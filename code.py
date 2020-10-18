import smtplib

# STMP -Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

frm_addr = 'your_id@your_domain.com'
to_addr  = ['abc@Your_domain.com' , 'xyz@your_domain.com']

msg = MIMEMultipart()

# add 'From' and 'To' headers and subject
msg['From']    = frm_addr
msg['To']      = ",".join(to_addr)
msg['subject'] = 'just to check'

body = '----Your message here ----'

#attach message
msg.attach(MIMEText(body,'plain'))

email    = 'your_id@your_domain.com'
password = 'password'

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()                #to identify yourself to ESMTP SERVER
mail.starttls()            # put STMP connection in TLS mode
mail.login(email,password) #log in on STMP server that require authentication

# message as string
text = msg.as_string()
mail.sendmail(frm_addr,to_addr,text)  #send mail
mail.quit()         #terminate SMTP session

print('Mail Sent')

