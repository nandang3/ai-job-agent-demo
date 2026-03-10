import smtplib
from email.mime.text import MIMEText
from datetime import date

report = open("../reports/daily_report.txt").read()

msg = MIMEText(report)
msg["Subject"] = f"AI Job Agent Report - {date.today()}"
msg["From"] = "nandang321@gmail.com"
msg["To"] = "nandang321@gmail.com"

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("nandang321@gmail.com","sanl kwcq rjvv mmjm")
server.send_message(msg)
server.quit()

print("Email sent.")
