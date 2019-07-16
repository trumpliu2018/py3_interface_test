import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from email.header import Header 
from test_config import config


def send_email(content, to_address):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = 'api robot'
    msg['To'] = config.MailUser
    msg['Subject'] = 'Api Test Report'

    try:
        smtp = smtplib.SMTP_SSL('smtp.163.com')
        smtp.login(config.MailUser, config.MailPwd)
        smtp.sendmail(config.MailUser, to_address, msg.as_string())
    except Exception as e:
        print(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email()
