import smtplib
from account import *
from random import *
from email.message import EmailMessage

nicknames = ["유재석", "박명수", "정준하", "정형돈", "하하"]


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        comtent = nickname + "/" + str(randint(1000,9999)) # 전화번호 4자리
        msg.set_content(comtent)

        smtp.send_message(msg)
        print(nickname + "님이 지원 완료")
