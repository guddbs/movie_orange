import math
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# anaconda prompt
# > conda activate cnu_python
# > pip install beautifulsoup
# > pip install selenium
# > pip install webdriver


##############################
# 1. install ChromDriver for selenium#
###########################################
# Selenium -> 개인 웹 브라우저 사용!(우리는 웹 브러우저 중 chorme 사용)
# Selenium -> webdriver(chrome)
# 1. 최신버전 사용해서 code로 다운로드(최신버전)
# 2. chrome driver 다운로드 후 주입(구버전)
# 주소 : https://sites.google.com/chromium.org/driver/




options = Options()
options.add_experimental_option("detach", True)   # ChromeDriver 자동종료 X
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)




######################################
# 2. Open URL in ChromeDriver #
######################################
# selenium: 동적 페이지에서 웹 크롤링 가능!
#           -> 원래 용도:웹 브라우저 텍스트 용

# http: 웹
# ftp : 파일전송
# ssh : 터미널 접속
# smtp : 메일 전송
movie_id = 160244
url = f"https://movie.daum.net/moviedb/grade?movieId={movie_id}"  # 물음표 앞까지만 주소

# Selenium의 ChromeDriver를 통해서 해당 URL 접속
driver.get(url)
time.sleep(1)   # 1초 딜레이(웹 페이지 랜더링 완료까지 기다리기)
doc_html = driver.page_source  # 해당 URL의 소스코드

doc = BeautifulSoup(doc_html, "html.parser")
title = doc.select("span.txt_tit")[1].text.strip()  # 영화제목 수집

# 전체리뷰: 91개
# 기존출력: 10개
# 1클릭 30개 추가
# (전체리뷰-기존출력) / 30 = 3(평점 더보기 클릭 횟수)

total_reveiw_txt = doc.select("span.txt_netizen")[0].text
# 정규화 -> 숫자만 추출
total_review = int(re.sub(r"[^~0-9]", "", total_reveiw_txt))  # 정교화  #

click_cnt = math.ceil((total_review - 10) / 30)   # "평점 더보기" 버튼 클릭 횟수(모든 리뷰 출력을 위한)

for i in range(click_cnt):
    # 평점 더보기 버튼 클릭(리뷰 : 30개씩 증가)
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)
time.sleep(5)

# >> 해당 페이지에 모든 리뷰 출력 완료
review_html = driver.page_source
doc = BeautifulSoup(review_html, "html.parser")
review_list = doc.select("ul.list_comment div.cmt_info")

for review_box in review_list:
    score = review_box.select("div.ratings")[0].text
    writer = review_box.select("")
    review_date = review_box.select("")
    review = review_box.select("")
    print(f"- 평점 : {score}")

# 숙제 : 리뷰, 작성자, 작성일자 수집!