# Flag Email Project - ATCS Final Project
# May 11, 2020

__author__ = 'Jack Preble'

import smtplib

'''Tutorials: 
https://www.youtube.com/watch?v=mP_Ln-Z9-XY
https://www.youtube.com/watch?v=Jbix9y8iV38&t=129s
https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/ **(Main Source)**
'''

from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

subject = 'hello'
msg = 'hello'

subject = 'This is a test'

def getContacts(f):
    global names, emails

    names = []
    emails = []

    with open(f, 'r') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])

    return names, emails

def read_template(filename):
    global names, emails

    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    global names, emails, subject

    names, emails = getContacts('mycontacts.txt')
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(config.address, config.password)

    for name, email in zip(names, emails):
        msg = MIMEMultipart('hello')

        message = message_template.substitute(PERSON_NAME = name.title())
        print(message)

        msg ['From'] = config.address
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg

    s.quit()

if __name__ == "__main__":
    main()
