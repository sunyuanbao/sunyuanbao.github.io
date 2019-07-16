from lxml import etree
from lxml import html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=chrome_options)
url='https://www.2345.com/?38264-0010'
driver.get(url)
html=driver.page_source
page=etree.HTML(html)
html = driver.page_source
page = etree.HTML(html)
sys=page.xpath('//*[@id="firstDayTemp"]/div[1]/a[1]//text()')
print(sys)

driver.quit()
