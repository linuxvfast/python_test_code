import smtplib,glob
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# COMMASPACE = ','
SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 25

def send_email(user,pwd,to,attach):
    msg = MIMEMultipart()
    msg['Subject'] = 'Our family reunion'  #标题
    msg['From'] = user
    msg['To'] = to
    msg.preamble = 'Our family reunion'
    # print(attach)
    for file in attach:
        fp = open(file,'rb')
        img = MIMEImage(fp.read())
        # print(len(img))
        fp.close()
        msg.attach(img)

    server_smtp = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    print('connecting to mail server')
    try:
        server_smtp.ehlo()
        print('starting encrypted seccion.')
        server_smtp.starttls()
        server_smtp.ehlo()
        print('logging to email server.')
        server_smtp.login(user,pwd)
        print('sending email.')
        server_smtp.sendmail(user,to,msg.as_string())
    except Exception as e:
        print('sending mail failed:{0}'.format(e))
    finally:
        server_smtp.quit()

def main():
    send_email('25556854@qq.com','ddndjfadfadlfjadf','test@263.com',['abc.png'])#收件人，开启qq发件的密码，发件人，附件名

if __name__ == '__main__':
    main()
