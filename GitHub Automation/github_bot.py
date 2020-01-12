from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GitHubBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password

    self.driver = webdriver.Chrome()

  
  def closeBrowser(self):
    self.driver.close()
  

  def login(self):
    # GitHub direct URL
    driver = self.driver
    driver.get('https://github.com/')
    time.sleep(2)
    # "//a[href='https://github.com/login']"
    login_btn = driver.find_element_by_link_text("Sign in")
    login_btn.click()
    time.sleep(2)
    # "//input[@name='login']"
    user = driver.find_element_by_xpath("//input[@name='login']")
    user.clear()
    user.send_keys(self.username)
    # "//input[@name='password']"
    passw = driver.find_element_by_xpath("//input[@name='password']")
    passw.clear()
    passw.send_keys(self.password)
    passw.send_keys(Keys.RETURN)
    time.sleep(2)


esau_ig = GitHubBot('esau-morais', 'A1B2CE20e')
esau_ig.login()