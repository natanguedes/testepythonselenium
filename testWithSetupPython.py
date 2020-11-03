from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\natan\\Downloads\\chromedriver.exe")

driver.execute_script("window.open('http://stackoverflow.com/', '_blank')")
