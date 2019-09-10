from selenium import webdriver
from selenium.webdriver.common.keys import Keys
f=open("info.txt", "r")
cont = f.read()
user = cont.split('\n')[0].split(' ')[2]
pwd = cont.split('\n')[1].split(' ')[2]
## Only for debugging purpose
#print(user)
#print(pwd)


driver = webdriver.Chrome()

# Uncomment this and comment the line above to use firefox instead of Google Chrome
#driver = webdriver.Firefox()

driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
