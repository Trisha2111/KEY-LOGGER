import smtplib,ssl

def send_email(message):
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="shwetamalani81@gmail.com"
    password="8987660500"
    receiver="shwetamalani81@gmail.com"
    context=ssl.create_default_context()
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver,message)
    except Exception as e:
        print(e)
    finally:
        server.quit()