import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.maximize_window()
chrome.get("https://elefant.ro")
time.sleep(3)
chrome.find_element(by=By.ID, value="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
# chrome.find_element(By.NAME, value="SearchTerm").send_keys("iphone")
# chrome.find_element(By.NAME, value="search").click()

chrome.find_element(By.XPATH, '//span[contains(@class, "login-prompt js-login-prompt")]').click()
time.sleep(1)
chrome.find_element(By.XPATH, '//a[contains(@class, "my-account-login btn btn-primary btn-block")]').click()

# time.sleep(5)
# chrome.find_element(By.ID, value="SortingAttribute").send_keys("Pret crescator")
# time.sleep(5)
# chrome.find_element(By.XPATH, '//div[contains(@class, "product-list-item")]').click()
time.sleep(30)
