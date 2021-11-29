from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=P4z1O3miesI")
domElement = driver.find_elements_by_class_name('style-scope yt-img-shadow')

for element in domElement :
    print(element.text())
