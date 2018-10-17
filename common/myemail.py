import sys
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import ConfigParser

def mysendemail(message):
    parser=ConfigParser.ConfigParser()
    #cfpath=os.path.dirname(os.path.abspath('.'))+'\\config\\config.ini'
    cfpath = os.path.abspath('.') + '\\config\\config.ini'
    parser.read(cfpath)

    fromaddr=parser.get('email', 'fromaddr')
    toaddr=parser.get('email', 'toaddr')
    pwd=parser.get('email', 'pwd')
    smtp_server=parser.get('email', 'smtp_server')
    smtp_port=parser.get('email', 'smtp_port')
    smtp_subject=parser.get('email', 'smtp_subject')
    smtp_body=message


    server=None
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = smtp_subject
        msg.attach(MIMEText(smtp_body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(fromaddr, pwd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except Exception, err:
        print("SMTP error: {}".format(err))
        return 1

    if server != None:
        server.close()

    return 0


if __name__ == "__main__":
    mysendemail("how is doing")
