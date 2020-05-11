# Flag Email Project - ATCS Final Project
# May 11, 2020

__author__ = 'Jack Preble'

import aiosmtplib

# Main tutorial: https://www.youtube.com/watch?v=mP_Ln-Z9-XY

subject = 'hello'
msg = 'hello'



def sendEmail(subject, msg):
    try:
        server = aiosmtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.address, config.password)
        message = "Subject: {}\n\n{}".format(subject,msg)
        server.sendmail(config.address, config.address, message)
        server.quit()
        print('Success')
    except:
        print('Failure')


if __name__ == "__main__":
    sendEmail(subject, msg)