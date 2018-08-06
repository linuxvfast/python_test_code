#发送纯文字邮件
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 25

def send_mail(user,pwd,to,subject,text):
    '''
    :param user:登录smtp服务器的账号
    :param pwd: 登录smtp服务器的密码
    :param to:收件人地址
    :param subject: 邮件的标题
    :param text: 邮件的内容
    :return:
    '''
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    smtp_server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    print('Connecting To Mail Server.')

    try:
        smtp_server.ehlo()
        print('Starting Encrypted Seccion.')
        smtp_server.starttls()
        smtp_server.ehlo()
        print('Logging Into Mail Server')

        smtp_server.login(user,pwd)
        print('Sending Mail.')
        smtp_server.sendmail(user,to,msg.as_string())
    except Exception as err:
        print('Sending Mail Failed:{0}'.format(err))
    finally:
        smtp_server.quit()

def main():
    send_mail('2559811312@qq.com','dfadjflajdlfa','tianyadong@315i.com','Important','Test Message')

if __name__ == '__main__':
    main()
