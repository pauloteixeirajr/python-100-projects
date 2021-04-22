from selenium import webdriver

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "/Users/paulot/Code/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
button = driver.find_element_by_class_name("btn")

fname.send_keys("Paulo")
lname.send_keys("Teixeira")
email.send_keys("paulo@email.com")
button.click()
