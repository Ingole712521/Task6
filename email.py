mport smtplib, ssl
import getpass

def email(password):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "****************@gmail.com"  # Enter your address
    receiver_email = "**************@gmail.com"  # Enter receiver address
    message = """\
    Subject: Hello From Python

    This is the Face of Omkar."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
