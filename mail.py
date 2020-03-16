import RPi.GPIO as GPIO
import time
import smtplib
import smbus
import sys
from email.mime.text import MIMEText
from email.utils import formatdate

#GPIO setup------------------------------------------------------------------

#mail set（アドレス等のメールを必要な情報）---------------------------------------------------------------------
FROM_ADDRESS = 'mbk1953.lab@gmail.com'
MY_PASSWORD = 'lcbeagdkvkncrhnn'        #Googleアカウントを2段階認証にしている関係で、ここは専用のアプリパスワードを使用している
TO_ADDRESS = 'tu-i-so.agaritakatta@ezweb.ne.jp'
BCC = 'mbk1953.lab@gmail.com'
SUBJECT = 'Error'
BODY = 'machine has stopped'

#message function（メールを作成する関数）-------------------------------------------------------------
def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg

#send function（メール送信関数）---------------------------------------------------------------
def send(from_addr, to_addrs, msg): 
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

#lux function（光センサからの光量を読み込む関数）----------------------------------------------------------------

#variable（変数の準備）--------------------------------------------------------------------
val_gpio23 = 0
old_val_gpio24 = 0
val_gpio24 =0
state = 0
old_sate = 0
old_get_lux = 0

#main------------------------------------------------------------------------
try:
    while True:
             to_addr = TO_ADDRESS
             subject = SUBJECT
             body = BODY


             msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
             send(FROM_ADDRESS, to_addr, msg)
             print('email sent')




except KeyboardInterrupt:
    print ('exit')

GPIO.cleanup()
