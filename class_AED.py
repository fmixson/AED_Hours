import selenium
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd


class SummerSession(object):
    # driver = webdriver.Chrome("C:/Users/53674/PycharmProjects/chromedriver.exe")

    def __init__(self, session):
        self.session = session

    def select_session(self):
        print('Hello, the session is', self.session)

    #
        global tr_table
        print(driver)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        table = soup.find('select', {'onchange': 'New_Term(this.form)', 'name': 'term_code'})
        option_table = table.find_all('option')
        drop_down = driver.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr/td[2]/form[1]/p/select/option[5]').click()

        for i in range(len(option_table)):
            semester = option_table[i].text
            if semester == self.session:
                y = i + 1
                print(f'y = {i + 1}')
                drop_down = driver.find_element_by_xpath(
                    '/html/body/table[2]/tbody/tr/td[2]/form[1]/p/select/option[' + str(y) + ']').click()
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'lxml')

                table = soup.find('table', {'bgcolor': 'white'})
                print(table)
                # table = soup.find('/html/body/table[2]/tbody/tr/td[2]/form[1]/p/select')
                tr_table = table.find_all('tr')
                print(tr_table)
                print(len(tr_table))




driver = webdriver.Chrome("C:/Users/53674/PycharmProjects/chromedriver.exe")
driver.get('https://secure.cerritos.edu/rosters/login.cgi')
login = driver.find_element_by_name('login')
login.send_keys('gvasquez')
login = driver.find_element_by_name('passwd')
login.send_keys('Celestino80!')
button = driver.find_element_by_xpath('//*[@id="login_form"]/table/tbody/tr[3]/td[2]/input').click()
#This waits for list of courses to load
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'clform')))
#
#
# # session = SelectSession(webdriver.Chrome(C:/Users/53674/PycharmProjects/chromedriver.exe), 'Summer 2020')
# session = SelectSession('2020 Summer')

p = SummerSession(session='2020 Summer')
p.select_session()


# s = Select('2020 Summer')
# s.session()
# headers = ['NO', 'Name', 'ID', 'Grade', 'Hours', 'Other', 'Section', 'Course']
# df = pd.DataFrame(columns=headers)
# pd.set_option('display.max_columns', None)


