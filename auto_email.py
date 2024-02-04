import smtplib

''' This Email generator is only for using email that are used to give data as an automator.
    Don't use personal email addresses for sending emails library not secure.
    Use 2 -factor authentication in email addresses instead to use your own personal email or make new email id.
'''

send_email_to = input('Send email to: ')
sender_email = input("Your email id: ")
password = input("Your password: ")
your_message = input('Your message: ')



def send_email(your_email, secret_password, to_email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(user=your_email, password=secret_password)
    server.sendmail(your_email, to_addrs=to_email, msg=message)


send_email(your_email=sender_email, secret_password=password, to_email=send_email_to, message=your_message)


