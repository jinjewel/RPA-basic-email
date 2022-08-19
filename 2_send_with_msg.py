import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "내 매일" # 받는사람

# # 여러명에게 메일을 보내야 할때
# msg["To"] = "1번 메일, 2번 메일, ..."
# to_list = ["1번 메일","2번 메일", "3번 메일"]
# msg["To"] = ", ".join(to_list) # ','를 구분해서 join 으로 메일들을 합친다.

# # 참조
# msg["Cc"] = "1번 메일" # 1번 사람에게 참조로 메일을 보낸다.

# # 비밀참조
# msg["Bcc"] = "2번 메일" # 2번 사람에게 비밀참조로 메일을 보낸다.

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수렵되는지 확인
    smtp.starttls() # 모든 내용이 암화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)
