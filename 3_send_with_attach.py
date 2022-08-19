import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는사람\
msg.set_content("다운로드 하세요.") # 본문

# msg.add_attachment()
# MIME Type
with open("myw3schoolsimage.jpg", "rb") as f:
    # 보내지는 파일이 .jpg 이라서 image/jpeg 로 설정함
    # 만약 .png 였으면, image/png 이였음
    msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=f.name)

with open("test.pdf", "rb") as f:
    # 보내지는 파일이 .pdf라서 application/pdf 로 설정함
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)    

with open("엑셀.xlsx", "rb") as f:
    # 보내지는 파일이 보통 기본적인 파일은 application/octet-stream 로 설정할수 있음
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)    

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수렵되는지 확인
    smtp.starttls() # 모든 내용이 암화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
    smtp.send_message(msg)