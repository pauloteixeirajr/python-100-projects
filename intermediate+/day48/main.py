from selenium import webdriver

chrome_driver_path = "/Users/paulot/Code/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://python.org")
events_list = driver.find_elements_by_css_selector(".event-widget li")
events = {}

for i, event in enumerate(events_list):
    time, name = event.text.split("\n")
    events[i] = {
        "time": time,
        "name": name,
    }

print(events)
# # price = driver.find_element_by_id("priceblock_ourprice")
# # driver.find_element_by_name("query")
# # driver.find_element_by_class_name("buttons")
# # driver.find_elements_by_css_selector(".documentation a")
# anchor = driver.find_element_by_xpath(
#     '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# print(anchor.text)

driver.quit()
