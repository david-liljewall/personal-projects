import smtplib
from email.message import EmailMessage


def email_alert( subject, body, to ):
    
    msg  = EmailMessage()
    msg.set_content( body )
    msg[ 'subject' ] = subject
    msg[ 'to' ] = to
    
    
    # use existing gmail account
    user = "davidliljewall96@gmail.com"
    password = "qmptnzejmrkbjndd" # provided Google app password (UNIQUE FOR THIS PROJECT)
    msg[ 'from' ] = user
    
    # login to server, use TLS inspection, login, then send desired message
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( user, password )
    server.send_message( msg )
    
    server.quit()
    
    
    
#* If main program running, run the code above. Won't run if imported
if __name__=='__main__':
    
    
    # create variables for email sending
    print( "Enter the desired recipient:" )
    recipient = input()
    
    print( "Enter the subject line:" )
    sub = input()
    
    print( "Enter the Email body text:" )
    bod = input()
    
    # call variables and send email
    email_alert( sub, bod, recipient )