from selenium import webdriver


driver = webdriver.Chrome('Z:\chromedriver')

class twitter:
    def post(self):
        driver.get('https://www.twitter.com/login')

        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys('id')
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys('pw')
        driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').submit()

        driver.find_element_by_xpath('//*[@id="global-new-tweet-button"]').click()
        driver.find_element_by_xpath('//*[@id="tweet-box-global"]').send_keys('test')
        driver.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[3]/div[2]/button').click()


if __name__ == '__main__':
    t = twitter()
    t.post()