
from selenium import webdriver


driver = webdriver.Chrome('Z:\chromedriver')


#access url
driver.get('https://www.facebook.com')

driver.find_element_by_name('email').send_keys('account')
driver.find_element_by_name('pass').send_keys('passwd')

driver.find_element_by_id('u_0_u').click()

driver.get('https://www.facebook.com/%ED%95%9C%ED%99%94-%EC%9D%B4%EA%B8%80%EC%8A%A4-%EC%8A%B9%ED%8C%A8-%EC%95%8C%EB%A6%BC-766948450152743/')

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="js_8"]/form/div[1]/div[2]/div/textarea').send_keys('test')
driver.implicitly_wait(5)

#driver.find_element_by_xpath('//*[@id="js_c0"]/div[2]/div[2]/div/div[2]/div/span[3]/div/button').click()
driver.find_element_by_class_name('_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft').click()