#-*- coding: utf-8 -*-
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def job():
    print("entered")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\ ~~~ \chromedriver.exe')

    #Linux: ex) /usr/bin/chromedriver
    #Windows: ex) r'C:\Users\username\Downloads\chromedriver_win32\chromedriver.exe'

    id="your id"
    pwd="your password"

    driver.get('https://hoc40.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=(your homepageid)')
    #Homepage ID : 클래스 들어간 후 ~ebssw.kr/(id)/hmpg ~

    login = driver.find_element_by_id("j_username")
    login.send_keys(id)
    login = driver.find_element_by_id("j_password")
    login.send_keys(pwd)
    driver.find_element_by_class_name('img_type').click()
    time.sleep(1)
    driver.get('https://hoc40.ebssw.kr/bddj0208/hmpg/hmpgBbsListView.do?menuSn=406433&bbsId=BBSID_000394784')
    #출석하는 곳(요일별 리스트)
    
    driver.find_elements_by_class_name('class_nm_ellipsis')[0].click()
    driver.find_element_by_tag_name('textarea').send_keys('출석') #.decode('utf-8')
    driver.find_element_by_class_name('submit').click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.quit()

sched = BlockingScheduler()
sched.add_job(job, 'cron', day_of_week='0-4', hour='8', minute='40')

'''
day_of_week : 0-4: 월-금
hour : 8시
minute : 40분
'''
sched.start()
