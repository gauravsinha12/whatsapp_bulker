from selenium import webdriver
import pyautogui as pg
import time
import pandas as pd
from config import CHROME_PROFILE_PATH

data = pd.read_csv("Gauravsdata.csv")
data_dict = data.to_dict('list')
leads = data_dict['Numbers']
messages = data_dict['Messages']
combo = zip(leads,messages)

first = True
for lead,message in combo:
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)
    browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe',options=options)
    time.sleep(1)
    browser.get('https://web.whatsapp.com/send?phone='+lead)
    time.sleep(7)
    texe = browser.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    texe.send_keys(message)
    time.sleep(1)
    buto = browser.find_element_by_class_name('_2Ujuu')
    buto.click()
    pg.hotkey('ctrl', 'w')
    time.sleep(2)
    pg.press('enter')
    print("Message sent to"+lead)
    if first:
        time.sleep(2)
        first=False

print("task completed")