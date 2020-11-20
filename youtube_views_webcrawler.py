from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

#webdriver_manager自動安裝Chrome版本對應的 Driver，並且設定好路徑和權限
chromedriver = ChromeDriverManager().install()

#迴圈須放在此位置
driver = webdriver.Chrome(chromedriver)

#youtube影片的網址
driver.get('https://www.youtube.com/watch?v=rfscVS0vtbw')


try:
    #等待10秒，直到 id="info-text" 出現
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'info-text')))
    
finally:
    #解析當下的網頁原始碼
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    
#印出該影片的觀看次數
print(soup.find('span',{'class':'view-count style-scope yt-view-count-renderer'}).string)

#driver.close()
