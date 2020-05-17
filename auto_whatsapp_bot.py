from selenium import webdriver
import time
from weather import weather


def auto_whatsapp_bot(name):
    driver = webdriver.Chrome()
    driver.get('http://web.whatsapp.com')

    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//*[text() = "{}"]'.format(name))

    user.click()

    msg_box = driver.find_element_by_class_name('_3u328 ')
    time.sleep(1)

    x = 2
    newmsg = ''

    while x == 2:

        group = driver.find_elements_by_class_name(
            'FTBzM')

        message = group[-1].find_element_by_class_name(
            '_12pGw').find_element_by_tag_name('span').find_element_by_tag_name('span').text
        message = message.lower()
        if message != newmsg:

            print(message)
            if message == 'hi':
                msg_box.send_keys('hello')
                driver.find_element_by_class_name('_3M-N-').click()
            if message == 'weather':
                msg_box.send_keys(f'temperature is {weather()} degrees')
                driver.find_element_by_class_name('_3M-N-').click()

        newmsg = message

        time.sleep(2)


auto_whatsapp_bot('Bablu')
