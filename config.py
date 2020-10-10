"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

# smtp settings
SMTP_HOST     = '__HOSTNAME__'
SMTP_PORT     = '___PORT___'
SMTP_USER     = '' # Leave empty if not needed
SMTP_PASSWORD = '' # Leave empty if not needed
ENCRYPT_MODE  = 'ssl' # Choose between 'none', 'ssl' and 'starttls'

# the address and name the email comes from
SENDER_NAME = 'SENDER_NAME_HERE'
SENDER_EMAIL = 'SENDER_EMAIL_HERE'
