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
driver = webdriver.Chrome("C:/Users/53674/PycharmProjects/chromedriver.exe")
driver.get('https://secure.cerritos.edu/rosters/login.cgi')
login = driver.find_element_by_name('login')
login.send_keys('gvasquez')
login = driver.find_element_by_name('passwd')
login.send_keys('Celestino80!')
button = driver.find_element_by_xpath('//*[@id="login_form"]/table/tbody/tr[3]/td[2]/input').click()
#This waits for list of courses to load
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'clform')))

headers = ['NO', 'Name', 'ID', 'Grade', 'Hours', 'Other', 'Section', 'Course']
df = pd.DataFrame(columns=headers)
pd.set_option('display.max_columns', None)

def select_session(y):
    drop_down = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/form[1]/p/select/option['+str(y)+']').click()

def rosters(start,finish):
    for i in range(start, finish):
        # This clicks on radio button to open roster
        counted_course = driver.find_element_by_xpath('//*[@id="clform"]/table/tbody/tr['+str(i)+']/td[2]').text
        # print(counted_course)
        if (counted_course != "AED 40.01") and ("IWAP" not in counted_course):
            pass
            # else:

        else:
            # print(counted_course)
            # button2 = driver.find_element_by_xpath('//*[@id="clform"]/table/tbody/tr[109]/td[1]/input').click()
            button2 = driver.find_element_by_xpath('//*[@id="clform"]/table/tbody/tr['+str(i)+']/td[1]/input').click()
            # This waits until roster open to run
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'college')))
            # This clicks on final grades link
            course = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[3]').text
            # print(course)
            cutup = course.split()
            # print(cutup)
            for word in cutup:
                if "(" in word:
                    section = word
            # section = cutup[4]
                    section = section[1:]
            # print(section)
            final_hours = driver.find_element_by_xpath('//*[@id="FinalGrades_form"]/a').click()
            course = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[3]').text
            # print(f'course{course}')
            # This waits until syllabus upload page loads
            course2 = cutup[0] + ' ' + cutup[1][:5]

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Roster_form')))
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')

            table = soup.find('table', {'bgcolor': 'white', 'cellpadding': '5', 'cellspacing': '0'})
            try:
                table2 = table.find_all('th')

            except:
                # print('exception')
                driver.back()
                driver.back()
                continue
            # print(f'table2{table2}')


            table3 = table.find_all('tr')[1:]
            # print(table3)
            for j in table3:
                raw_data = j.find_all('td')
                row = [tr.text for tr in raw_data]
                row.append(section)
                row.append(course2)
                # print(row)
                try:
                    length = len(df)
                    df.loc[length] = row
                except:
                    continue


            driver.back()
            driver.back()
        print(df)
        df.to_csv('C:/Users/53674/Desktop/Spreadsheets/IWPA_Raw_Data' + str(z) +'.csv')
        section_list = []
        for i in range(len(df)):
            if df.loc[i,'Section'] not in section_list:
                section_list.append(df.loc[i, 'Section'])

        headers2 = ['Course', 'Section', 'Total']
        # print(section_list)
        df_sections = pd.DataFrame(columns=headers2)
        # section_hours = []
        for section in section_list:
            total_hours = 0
            section_hours = []
            for i in range(len(df)):
                if section == df.loc[i,'Section']:
                    course3 = df.loc[i, 'Course']
                    hours = df.loc[i,'Hours']
                    print(hours)
                    hours = hours.split()
                    print(hours)
                    hours = hours[0]
                    print(hours)
                    hours = float(hours)
                    print(hours)
                    total_hours = total_hours + hours
            section_hours.append(course3)
            section_hours.append(section)
            section_hours.append(total_hours)# section_hours[section] = total_hours
            # print(section_hours)
            length = len(df_sections)
            df_sections.loc[length] = section_hours
    print(df_sections)
    df_sections.to_csv('C:/Users/53674/Desktop/Spreadsheets/IWPA_Section_Totals' + str(z) +'.csv')

z = 1
select_session(5)
rosters(1, 100)
select_session(3)
rosters(1, 100)
# z = z + 1
# rosters(316,716)