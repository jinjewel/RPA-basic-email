from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") # initial_folder="INBOX" : 수신함

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:

    # for msg in mailbox.fetch(limit=5, reverse=True): # 전체메일 다 가져오기
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True): # 읽지 않은 메일 가져오기
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # for msg in mailbox.fetch('(FROM bm302512@gmail.com)',limit=1, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 항상 형식, 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 튼따옴표로 감싸야된다.
    # for msg in mailbox.fetch('(TEXT "test mail")',limit=5, reverse=True): # 특정 글자를 포함하는 메일 가져오기 (제목, 본문)
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test mail")', reverse=True): # 특정 글자를 포함하는 메일 가져오기 (제목만)
    #     print("[{}] {}".format(msg.from_,msg.subject))

    # 한글을 키워드로 하는 검색는 우회방법
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_,msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 07-Aug-2022)', limit=5, reverse=True): # 특정 날짜 이후의 메일 가져오기
    #     print("[{}] {}".format(msg.from_,msg.subject))           

    # for msg in mailbox.fetch('(ON 19-Aug-2022)', limit=5, reverse=True): # 특정 날짜에 온 메일 가져오기
    #     print("[{}] {}".format(msg.from_,msg.subject))  

    # 두가지 이상의 조건을 모두 만족하는 메일 가져오기 (예. 특정 제목을 가지고 당일에 온 메일))
    for msg in mailbox.fetch('(ON 19-Aug-2022 SUBJECT "test mail")', limit=5, reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))  

    # 두가지 이상의 조건을 하나라도 만족하는 메일 가져오기 (예. 특정 제목을 가지거나 당일에 온 메일))
    for msg in mailbox.fetch('(OR ON 19-Aug-2022 SUBJECT "test mail")', limit=5, reverse=True):
        print("[{}] {}".format(msg.from_,msg.subject))      