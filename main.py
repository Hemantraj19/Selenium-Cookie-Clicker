from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

duration = 300
start_time = time.time()
diff = 0
last_check_time = start_time
while diff < duration:
    diff = time.time() - start_time
    cookie.click()
    if time.time() - last_check_time >= 5:
        stores = driver.find_elements(By.CSS_SELECTOR, "div #store div:not(.grayed)")
        stores[-1].click()
        last_check_time = time.time()

cookie_per_s = driver.find_element(by=By.ID, value="cps").text
print(cookie_per_s)
driver.quit()
