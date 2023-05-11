#settings
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

import requests as req
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import csv


#debugging modept
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/김경진/Desktop/NEXT/NEXT-HW/Session5/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

#webpage
driver.get('https://movie.daum.net/main')
driver.implicitly_wait(5)

#영화 랭킹페이지로 이동
search_ranking=driver.find_element(By.XPATH, '//*[@id="gnbContent"]/ul/li[2]/a')
search_ranking.click()
driver.implicitly_wait(3)

titles=[]
genres=[]
directors=[]
ratings=[]
for i in range(1, 21): 
    
      movie_element=driver.find_element(By.XPATH, f'//*[@id="mainContent"]/div/div[2]/ol/li[{i}]/div/div[2]/strong/a')
      movie_element.click()
      driver.implicitly_wait(3)
      soup = BeautifulSoup(driver.page_source, 'html.parser')
      #soup
      title = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_tit > h3 > span.txt_tit').text.strip()
      genre = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(1) > dl:nth-child(2) > dd').text.strip()
      rating = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(2) > dl:nth-child(1) > dd').text.strip()
      #list
      titles.append(title)
      genres.append(genre)
      ratings.append(rating)
      try:
           director = soup.select_one('#mainContent > div > div.box_detailinfo > div.contents > div.detail_crewinfo > ul > li:nth-child(1) > div > div > strong > a').text.strip()
      except:
           director =('None')
      directors.append(director)
     
      driver.back()
      driver.implicitly_wait(3)

# 리스트를 행렬로 변환
rows = zip(titles, genres, ratings)

# csv 파일에 저장
with open('movie.csv', mode="w", newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerow(["title", "genre", "rating"])
     writer.writerows(rows)

#좋아하는 영화 검색
# search_box = driver.find_element(By.XPATH, './html/body/div[2]/header/div[3]/div/a')
# search_box.send_keys('어바웃타임')
# search_box.send_keys(Keys.ENTER)
# driver.implicitly_wait(3)
# movie_element=driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[2]/ul/li[1]/div/div/strong/a')
# movie_element.click()

# title = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_tit > h3 > span.txt_tit').text.strip()
# genre = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(1) > dl:nth-child(2) > dd').text.strip()
# rating = soup.select_one('#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(2) > dl:nth-child(1) > dd').text.strip()
# movie_element=driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a/span')
# movie_element.click()
# comment = soup.select_one('#mainContent > div > div.box_detailinfo > div.contents > div > strong > span')





       

