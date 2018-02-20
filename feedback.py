'''
Author : Akshay chauhan
Description : This script only works with firefox, for other browser support change webdriver.Firefox()
Reference : http://selenium-python.readthedocs.io/
'''
intro='''
\t\t\t\t\t ^^^^^ @miz0ne feedback automation ^^^^^\n
\t\t\t\t\t@author Akshay chauhan | @IG mr.akin.o
\n
Note: This application is made for educational purpose only.
      Use of this tool for malicious purposes is strictly prohibited. Also i highly recommend to fill the feedback form
      by your own instead of using this tool since they are made for the betterment of university.

**** AUTHOR OF THIS APP DOES NOT SUPPORT USE OF THIS TOOL FOR FILLING THE FEEDBACK FORMS ****
'''
print(intro)
confirmation=input('>>Should i proceed? (type yes or no)').lower()

if confirmation!='yes':
    exit(0)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
url="https://amizone.net/Amizone/index.aspx"
feeback_url='https://amizone.net/Amizone/WebForms/FacultyFeeback/FacultyFeedback.aspx'
insta='https://goo.gl/2SUF9B'
print('initializing process...')

try:
    driver=webdriver.Firefox()

except:
    print('Please install Mozilla firefox to use this tool!')
    print('Download : https://goo.gl/ngnmzw')
    exit(1)
print('browser started...')
print('opening url...')
driver.get(url)
print('waiting for login...')
try:
    user_name = WebDriverWait(driver, 12220).until(
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
        driver.implicitly_wait(3)
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
    print('\nCongrats! Feedback completed. Feeling like a hacker? :p :p  \n')
    #print(ex)
    print('**Follow me on instagram @mr.akin.o**')
    driver.get(insta)
    #driver.close()
input('Enter to close!')
#driver.close()
