
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
    
    
    # Attach Files
    files = [ 'mars_terraformed.jpg', 'attach_file.txt' ]
    
    for file in files:
        # Loop through files list created above
        with open( file, 'rb' ) as f:
            file_data = f.read()
            file_name = f.name

    msg.add_attachment( file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    
    
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