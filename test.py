from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
baseUrl = "http://www.allitebooks.com/page/1/?s=python"
driver.get(baseUrl)
# wait = WebDriverWait(driver, 5)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-result-list li")))
# Get last page number
lastPage = int(driver.find_element(By.CSS_SELECTOR, ".pagination a:last-child").text)
# Get all HREFs for the first page and save them in hrefs list
js = 'return [...document.querySelectorAll(".entry-title a")].map(e=>e.href)'
hrefs = driver.execute_script(js)
# Iterate throw all pages and get all HREFs of books
for i in range(2, lastPage):
    driver.get("http://www.allitebooks.com/page/" + str(i) + "/?s=python")
    hrefs.extend(driver.execute_script(js))
for href in hrefs:
    print(href)
