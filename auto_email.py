import smtplib


def send_email(sender_email, secret_password, receiver_email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(user=sender_email, password=secret_password)
    server.sendmail(sender_email, to_addrs=receiver_email, msg=message)




send_email('dhruvkarandikar124@gmail.com', '', 'ncefgtfvkhlssvtmfp@ckptr.com', 'Test Email')


