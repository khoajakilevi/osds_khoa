from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo Webdriver
driver = webdriver.Chrome()

# Mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)

# Đợi khoảng chừng 2 giây
time.sleep(2)

# Lay tat ca cac the <a> voi title chua "List of painters"
tags = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters')]")

# Tao ra danh sach cac lien ket
links = [tag.get_attribute("href") for tag in tags]

# Xuat thong tin
for link in links:
    print(link)

# Dong webdriver
driver.quit()