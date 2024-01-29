
import smtplib
import getpass #hide password when entering

# Set up email 
sender_email = "ai17c@gmail.com"
sender_password = "Dpl302m"

# Địa chỉ email người nhận
receiver_email = "duigoctu@gmail.com"

# Khởi tạo SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, "vqfc ndju oapv ijuh")

# Đăng nhập vào tài khoản email
server.login(sender_email, sender_password)
def send_email():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Stranger Detected"

    body = "Stranger detected ."
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail(sender_email, receiver_email, msg.as_string())