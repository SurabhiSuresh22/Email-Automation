import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

frm_addr = 'surabhisuresh2000@gmail.com'
to_addr = ['basilsaji222@gmail.com' , 'surabhi2207200@gmail.com']

msg = MIMEMultipart()
msg['From'] = frm_addr
msg['To'] = ",".join(to_addr)
msg['subject'] = 'just to check'

body = 'Hi guys'

msg.attach(MIMEText(body,'plain'))

email ='surbhisuresh2000@gmail.com'
password ='Suchi@22'

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(frm_addr,to_addr,text)
mail.quit()

'''from selenium import webdriver
from time import sleep

driver = None
driver = webdriver.Firefox()
SENDER = 'Surabhi S'
GMAIL_USER = 'surbhisuresh2000@gmail.com'
GMAIL_PASSWORD = 'Suchi@22'
MESSAGE = 'I will get back to you soon. \n Thanks'

def login_google():
    is_logged_in = False
    google_login = 'https://accounts.google.com/Login#identifier'
 
    try:
        driver.get(google_login)
        sleep(5)
        html = driver.page_source.strip()
 
        # email box
        user_name = driver.find_element_by_id('Email')
        if user_name:
            user_name.send_keys(GMAIL_USER)
 
        next = driver.find_element_by_id('next')
        if next:
            next.click()
 
        # give em rest
        sleep(5)
 
        # now enter passwd
        user_pass = driver.find_element_by_id('Passwd')
        if user_pass:
            user_pass.send_keys(GMAIL_PASSWORD)
 
        # rest again
        sleep(3)
 
        sign_in = driver.find_element_by_id('signIn')
        if sign_in:
            sign_in.click()
 
        # rest again
        sleep(3)
        html = driver.page_source.strip()
        is_logged_in = True
 
    except Exception as ex:
        print(str(ex))
        is_logged_in = False
    finally:
        return is_logged_in


user_name = driver.find_element_by_id('Email')
if user_name:
   user_name.send_keys(GMAIL_USER)
next = driver.find_element_by_id('next')
if next:
 next.click()


def access_gmail():
    try:
        driver.get('http://gmail.com')
        sleep(5)
        m = driver.find_elements_by_css_selector('.UI table > tbody > tr')

        for a in m:
            if SENDER.lower() in a.text:
                a.click()
                break

        # take rest
        sleep(5)
        reply = driver.find_element_by_css_selector('.amn > span')
        sleep(5)
        if reply:
            reply.click()
            sleep(1)

            editable = driver.find_element_by_css_selector('.editable')
            if editable:
                editable.click()
                editable.send_keys(MESSAGE)

            send = driver.find_elements_by_xpath('//div[@role="button"]')
            for s in send:
                if s.text.strip() == 'Send':
                    s.click()

    except Exception as ex:
        print(str(ex))
    finally:
        return True


m = driver.find_elements_by_css_selector('.UI table &gt; tbody &gt; tr')'''
