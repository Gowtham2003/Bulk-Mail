import csv, smtplib, ssl
import json
import config  # Our file config.py
from Message import Message

class Mailer:
    def __init__(self,HOST=None,PORT=None,ENCRYPT_MODE=None,username=None,password=None):
        self.HOST = HOST
        self.PORT = PORT
        self.ENCRYPT_MODE = ENCRYPT_MODE
        self.username = username
        self.password = password

    def getFromCSV(self,FILE_PATH):
        with open(FILE_PATH) as file:
            reader = csv.reader(file)
            return list(reader)
    
    def getFromJSON(self,FILE_PATH):
        with open(FILE_PATH,"r") as file:
            data = json.loads(file.read())
            if type(data) is not list:
                raise Exception(f"JSON Data Must be A list of Dicts/Objects not {type(data)}")
            else:
                data = [list(x.values()) for x in data]
                print(data)
                return data

    def send(self,message,receivers):
       context = ssl.create_default_context()
       MODE = self.ENCRYPT_MODE
       if MODE != 'none' and MODE != 'ssl' and MODE != 'starttls':
           raise Exception("Please choose a correct ENCRYPT_MODE")
       try:
           if self.ENCRYPT_MODE == 'ssl':
               server = smtplib.SMTP_SSL(host=self.HOST, port=self.PORT, timeout=10,context=context)
           else:
               server = smtplib.SMTP(host=self.HOST, port=self.PORT, timeout=10)

           if self.ENCRYPT_MODE == 'starttls':
               server.starttls()
               server.ehlo()


           server.login(self.username, self.password)

           
           for name, email in receivers:
               # print(message.as_string())
               server.sendmail(
                        message.getSender(),
                        email,
                        message.as_string()
                    )
       except Exception as e:
            print(e)
            exit(-1)

