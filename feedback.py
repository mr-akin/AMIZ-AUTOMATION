'''
Author : Akshay chauhan
Description : This script only works with firefox, for other browser support change line 15
Reference : http://selenium-python.readthedocs.io/
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
url="https://amizone.net/Amizone/index.aspx"
feeback_url='https://amizone.net/Amizone/WebForms/FacultyFeeback/FacultyFeedback.aspx'
print('initializing...')
driver=webdriver.Firefox()
print('started...')
driver.get(url)
print('waiting for login...')
try:
    user_name = WebDriverWait(driver, 220).until(
            EC.presence_of_element_located((By.ID ,"ctl00_lblUser"))
            )
    #print(user_name.get_attribute("innerhtml"))
    print('login success!')
    print('opening Faculty Feedback page...')
    driver.get(feeback_url)
    #elem_faculties=driver.find_elements_by_xpath('//input[@title="Please click here to give faculty feedback"]')
    #for _ in elem_faculties[:4]:
    while True:
        elem_faculty=driver.find_element_by_xpath('//input[@title="Please click here to give faculty feedback"]')
        elem_faculty.click()
        driver.implicitly_wait(4)
        submit=driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSubmit')
        input_elems=driver.find_elements_by_xpath('//input[@type="radio"][@value="4"]')
        input_ques=driver.find_elements_by_xpath('//input[@type="radio"][@value="1"]')
        input_ques.reverse()
        text_area=driver.find_element_by_xpath('//textarea')
        for e in input_elems:
            e.click()
        for e in input_ques[:4]:
            e.click()
        text_area.send_keys('comment!')
        submit.click()
#input('next?')
except Exception as ex:
    print('Error occured or process completed!')
    print(ex)
    #driver.close()
# *************  click CheckBox  ***************
input('Enter to close!')
driver.close()
