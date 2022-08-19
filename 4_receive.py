# pip install imap-tools

from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") # initial_folder="INBOX" : 수신함

for msg in mailbox.fetch(limit=1, reverse=True): # limit=1 : 받아오는 메일 수를 지정, reverse=True : 메일의 날짜순을 최근 메일부터 가지고 옴
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("="*100)

    # 첨부 파일
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        # 파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))


mailbox.logout()