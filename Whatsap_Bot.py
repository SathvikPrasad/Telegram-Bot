from selenium import webdriver
import time


def Whatsap_bot(name, msg, count):
    driver = webdriver.Chrome()
    driver.get('http://web.whatsapp.com')

    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//*[text() = "{}"]'.format(name))

    user.click()

    msg_box = driver.find_element_by_class_name('_3u328 ')

    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_class_name('_3M-N-').click()


# Whatsap_bot('Bablu', 'i am croton the king', 25)
