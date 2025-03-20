from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://forklog.com/news')
first_news = driver.find_element(By.XPATH, '(//*[@class="cell"]//a)[1]')
first_news_url = first_news.get_attribute('href')

with open('news.txt', 'w') as news_file:
    news_file.write(first_news_url)

