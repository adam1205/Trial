def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail-Yo"


send_email('kajari.gupta@gmail.com', 'simpletonmamma', 'siddharthsatpathy.ss@gmail.com', 'Coma Working', 'I love Python!')  

#import smtplib
#
#fromaddr = 'kajari.gupta@gmail.com'
#toaddrs  = 'siddharthsatpathy.ss@gmail.com'
#msg = 'Why,Oh why!'
#username = 'kajari.gupta@gmail.com'
#password = 'simpletonmamma'
#server = smtplib.SMTP('smtp.gmail.com:587')
#server.ehlo()
#server.starttls()
#server.login(username,password)
#server.sendmail(fromaddr, toaddrs, msg)
#server.quit()      
