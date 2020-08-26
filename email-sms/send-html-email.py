
import smtplib
from email.message import EmailMessage
import imghdr


def email_alert( subject, body, to ):
    
    # Set email message variables:
    msg  = EmailMessage()
    msg[ 'subject' ] = subject
    msg[ 'to' ] = to
    msg.set_content( body )
    
    
    # use existing gmail account
    user = "davidliljewall96@gmail.com"
    password = "qmptnzejmrkbjndd" # provided Google app password (UNIQUE FOR THIS PROJECT)
    msg[ 'from' ] = user

    
    msg.add_alternative( """\
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:SlateGray;">This is an HTML Email!<h1>
            </body>
        </html>                    
    """, subtype='html' )    
    
    # login to server, use TLS inspection, login, then send desired message
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( user, password )
    server.send_message( msg )

    
    # quit server
    server.quit()
    

    
# ---- If main program running, run the code above. Won't run if imported ---- #

if __name__=='__main__':
    
    
    # create variables for email sending
    print( "Enter the desired recipient:" )
    recipient = input()
    
    print( "Enter the subject line:" )
    sub = input()

    print( "Enter the email body:" )
    bod = input()
    
    # call variables and send email
    email_alert( sub, bod, recipient )