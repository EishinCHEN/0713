import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "applejack9972@gmail.com"
receiver = ["shjes945211@gmail.com", "applejack9972@gmail.com"]

for rece in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = rece
    header = Header("Test Send Email", "utf-8")
    msg["Subject"] = header.encode()

    body = "This is email send from python"
    msg.attach(MIMEText(body))

    ssl_context = ssl.create_default_context() ##連線
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context) as server:
        server.login(sender, "onft gyae mfjf igah")
        server.sendmail(sender, rece, msg.as_string())

    print("send email success") 