from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re 

class Message:
    def __init__(self,From=None,To=None,Subject=None):
        self.message = MIMEMultipart()
        self.message["From"] = From
        self.message["Subject"] = Subject
    
    def replace_placeholders(self,text,values):
        if values is None:
            return text.replace("{}","")
        try:
            return text.format(*values)
        except Exception as e:
            print("Error in Given Amount of Curly Braces")
            exit(-1)

    def createBody(self,content,values=None):
        body = self.replace_placeholders(content,values)
        body = MIMEText(body, "plain")
        
        return self.message.attach(body)


    def createHtmlBody(self,content,values=None):
        body = self.replace_placeholders(content,values)
        body = MIMEText(body, "html")
        return self.message.attach(body)

    def attachfile(self,filename):
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream

            # Email client can usually download this 
            # automatically as attachment
            email_content = MIMEBase("application", "octet-stream")
            email_content.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(email_content)

        # Add header as key/value pair to attachment email_content
        email_content.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message
        return email_content
    

    def as_string(self):
        return self.message.as_string()

    def getSender(self):
        return self.message["FROM"]

