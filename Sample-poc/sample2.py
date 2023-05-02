from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver = "D:\Windows\Download\chromedriver_win32"
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.cwb.gov.tw/V7/')
driver.set_window_position(0, 0)  # 瀏覽器位置
driver.set_window_size(700, 700)  # 瀏覽器大小

select = Select(driver.find_element_by_id('home-select-town'))
# driver.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
