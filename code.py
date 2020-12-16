import smtplib

# STMP -Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmail():
	# ask user to insert email and password
	USER_ = input('Enter Username: ')
	PASS_ = input('Enter Password: ')
	SERVER_ = input('Gmail / Outllook: ')
	RECiPIENTS_ = input('Enter Recipients seperated by comma: ').split(',')
	SUBJ_ = input('Enter Subject: ')
	BODY_ = input('Enter Content: ')

	if USER_ != "" and PASS_ != "" and SERVER_ != "" and RECiPIENTS_ != "" and SUBJ_ != "" and BODY_ != "" :

		if SERVER_ in ['Gmail', 'Outlook']:

			if SERVER_ == 'Gmail':
				mail = smtplib.SMTP('smtp.gmail.com',587)
			else:
				mail = smtplib.SMTP('smtp.office365.com',587)

			try:
				mail.ehlo()                #to identify yourself to ESMTP SERVER
				mail.starttls()            # put STMP connection in TLS mode
				mail.login(USER_,PASS_) #log in on STMP server that require authentication

				msg = MIMEMultipart()

				# add 'From' and 'To' headers and subject
				msg['From']    = USER_
				msg['To']      = ",".join(RECiPIENTS_)
				msg['subject'] = SUBJ_

				#attach message
				msg.attach(MIMEText(BODY_,'plain'))

				# message as string
				text = msg.as_string()
				mail.sendmail(USER_,RECiPIENTS_,text)  #send mail
				mail.quit()         #terminate SMTP session

				print('Mail Sent')
			except Exception as e:
				print("="*30)
				print(str(e))
				sendEmail()

		else:
			print("="*30)
			print('Please select Gmail/Outlook')
			sendEmail()
	else:
		print("="*30)
		print('All fields are required')
		sendEmail()


if __name__ == "__main__":
	sendEmail()




