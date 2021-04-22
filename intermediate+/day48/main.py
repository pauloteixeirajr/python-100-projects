from selenium import webdriver

chrome_driver_path = "/Users/paulot/Code/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.amazon.co.uk")

driver.quit()
