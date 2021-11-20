import selenium,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
password=raw_input('PASSWORD PLEASE   --  ')
driver = webdriver.Chrome('/home/ip-d/Documents/tinder/chromedriver')
driver.set_window_size(1700, 700)
# chrome_options = Options()
# chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
# driver = webdriver.Chrome('/home/ip-d/Documents/tinder/chromedriver',chrome_options=chrome_options)
driver.get('https://tinder.com')
time.sleep(5)

driver.execute_script("window.open('http://fb.com', 'new_window')")
driver.switch_to_window(driver.window_handles[1])

print('hello nov 2021')
email=driver.find_element_by_id("email")

email.send_keys('dhneshwod@gmail.com')

passw=driver.find_element_by_id("pass")

passw.send_keys(password)
driver.find_element_by_id("loginbutton").click()
driver.switch_to_window(driver.window_handles[0])

# time.sleep(5driver.switch_to_window(driver.window_handles[0])
modal=driver.find_element_by_id("modal-manager")
element2=modal.find_element_by_xpath(".//button[@aria-label='Login with Facebook']")
element2.click()

# print (dir(driver))
time.sleep(8)
elem = driver.find_elements_by_class_name('button__text')
# for i,ead in enumerate(elem):
#     print(i)
#     print(ead.text)
elem[5].click()
time.sleep(1)
elem = driver.find_elements_by_class_name('button__text')
elem[5].click()
time.sleep(1)
elem = driver.find_elements_by_class_name('button__text')
elem[5].click()
time.sleep(1)
elem = driver.find_elements_by_class_name('button__text')
elem[5].click()
time.sleep(1)
# driver.send_keys("", Keys.ARROW_RIGHT)
elem = driver.find_elements_by_class_name('button__text')
# for i,ead in enumerate(elem):
#     print(i)
#     print(ead.find_elements_by_tag_name('svg'))
#     print(ead.text)
# elem[4].click()
for i in range(0,1000):
    time.sleep(2)
    elem[3].click()
# tagNames = driver.find_elements_by_tag_name('button')
# for i,ead in enumerate(tagNames):
    # print(i)
# ead[5].click()
# time.sleep(2)
    # print(ead.text)
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# # print(tagNames)
# for i in tagNames:
#     print(i.get_attribute('aria-label'))
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# su=driver.find_element_by_class_name('onboarding__buttons')
#
# print 'ss',su
# try:
#     elem=su.find_element_by_xpath(".//button[@aria-label='Great!']")
#     elem.click()
# except:
#     print 'in except'
#     elem=su.find_element_by_xpath(".//button[@aria-label='Next']")
#     elem.click()
# print (len(driver.window_handles))
# print (dir(driver.window_handles))
#
# window_before = driver.window_handles[0]
# window_after = driver.window_handles[2]
# driver.switch_to_window(window_after)
# time.sleep(2)
# email = driver.find_element_by_id("email")
# passw = driver.find_element_by_id("pass")
#
# email.send_keys('9780329759')
# passw.send_keys("32@#hs5991inAT")
#
# loginin = driver.find_element_by_name('login')
# loginin.click()


# driver.quit()
