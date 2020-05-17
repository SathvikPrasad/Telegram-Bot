from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait


import time


def Telegram_Bot(phone, name, msg, count):
    driver = webdriver.Chrome()
    driver.get('https://web.telegram.org/#/login')
    phone_number = phone
    time.sleep(5)
    phone_num_text = driver.find_element_by_name('phone_number')
    phone_num_text.send_keys(phone_number)
    submit = driver.find_element_by_class_name('login_head_submit_btn')
    time.sleep(3)
    submit.click()
    time.sleep(3)
    conform = driver.find_element_by_class_name('btn-md-primary')
    conform.click()
    code = int(input('enter Code:'))
    time.sleep(5)
    code_input = driver.find_element_by_class_name('md-input')
    code_input.send_keys(code)
    time.sleep(5)
    user = driver.find_element_by_xpath('//*[text() = "{}"]'.format(name))
    user.click()
    for i in range(count):

        text_area = driver.find_element_by_class_name("composer_rich_textarea")
        text_area.send_keys(msg)
        time.sleep(3)
        button_send = driver.find_element_by_class_name("im_submit_send")
        button_send.click()


Telegram_Bot(9502402016, 'pc', 'hello how are you', 15)
