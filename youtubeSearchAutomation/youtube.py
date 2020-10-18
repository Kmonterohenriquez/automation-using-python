from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./drivers/chromedriver.exe')
driver.get('https://www.youtube.com')
searchbox  = driver.find_elements_by_id('search')
searchbox.send_keys('Sech')
searchbox.send_keys(Keys.ENTER)
video = driver.find_elements_by_link_text('Sech - La Despedida (Video Oficial)')
video.click()

# searchbox = driver.find_element_by_xpath('//*[@id="search"]')

# searchbox.click().send_keys('Sech')

# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchButton.click()