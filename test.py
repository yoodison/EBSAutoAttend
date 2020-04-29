#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from apscheduler.schedulers.blocking import BlockingScheduler

import time

def job():
    print("entered")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Users\yoodi\Downloads\chromedriver_win32\chromedriver.exe')

    #/usr/bin/chromedriver
    #r'C:\Users\yoodi\Downloads\chromedriver_win32\chromedriver.exe'

    id="yoodison"
    pwd="dbeltms5646"

    driver.get('https://hoc40.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=bddj0208')

    login = driver.find_element_by_id("j_username")
    login.send_keys(id)
    login = driver.find_element_by_id("j_password")
    login.send_keys(pwd)
    driver.find_element_by_class_name('img_type').click()
    time.sleep(1)
    driver.get('https://hoc40.ebssw.kr/bddj0208/hmpg/hmpgBbsListView.do?menuSn=406433&bbsId=BBSID_000394784')
    driver.find_elements_by_class_name('class_nm_ellipsis')[0].click()
    driver.find_element_by_tag_name('textarea').send_keys('출석') #.decode('utf-8')
    driver.find_element_by_class_name('submit').click()
    alert = driver.switch_to.alert
    alert.accept()

    driver.quit()

def job2():
    print("entered")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Users\yoodi\Downloads\chromedriver_win32\chromedriver.exe')

    #/usr/bin/chromedriver
    #r'C:\Users\yoodi\Downloads\chromedriver_win32\chromedriver.exe'

    id="ssh030507"
    pwd="shson0507"

    driver.get('https://hoc40.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=biolee7')

    login = driver.find_element_by_id("j_username")
    login.send_keys(id)
    login = driver.find_element_by_id("j_password")
    login.send_keys(pwd)
    driver.find_element_by_class_name('img_type').click()
    time.sleep(1)
    driver.get('https://hoc40.ebssw.kr/biolee7/hmpg/hmpgBbsListView.do?menuSn=344959&bbsId=BBSID_000371040')
    driver.find_elements_by_class_name('class_nm_ellipsis')[0].click()
    driver.find_element_by_tag_name('textarea').send_keys('출석') #.decode('utf-8')
    driver.find_element_by_class_name('submit').click()
    alert = driver.switch_to.alert
    alert.accept()

    driver.quit()
sched = BlockingScheduler()
sched.add_job(job, 'cron', day_of_week='0-4', hour='10', minute='57')
sched.add_job(job2, 'cron', day_of_week='0-4', hour='10', minute='58')

sched.start()