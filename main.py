from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import time

driver = webdriver.Chrome('Z:\chromedriver')

class twitter:
    def __init__(self):
        self.twit = driver
        self.twit.get('https://www.twitter.com/login')

    def login(self):
        self.twit.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys('email')
        self.twit.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys('passwd')
        self.twit.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').submit()

    def post(self, post = "test"):

        self.twit.find_element_by_xpath('//*[@id="global-new-tweet-button"]').click()
        self.twit.find_element_by_xpath('//*[@id="tweet-box-global"]').send_keys(post)
        self.twit.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[3]/div[2]/button').click()
        time.sleep(3)
        self.twit.get('https://twitter.com/')

class db:
    pass

class getRecord:
    def wl(self):
        pass

    def GetLinUp(self):
        Lineup = ""
        Lineup2 = ""

        driver.get('http://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&gameId=20170811SSHH02017')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        driver.find_element_by_xpath('//*[@id="away_lineup_btn"]').click()

        Lineup += driver.find_element_by_xpath('//*[@id="lineup_box"]/h3').text
        Lineup += "\n"
        Lineup += "선발투수" + "  " + driver.find_element_by_xpath('//*[@id="lineup_pitcher_player_0"]/td[1]/div/a').text
        Lineup += "\n"

        for x in range(0, 9):
            Lineup += str(x+1) + "  "
            Lineup += driver.find_element_by_xpath('//*[@id="lineup_batter_player_{}"]/td[3]'.format(x)).text
            Lineup += "  "
            Lineup += driver.find_element_by_xpath('//*[@id="lineup_batter_player_{}"]/td[2]/div/a'.format(x)).text
            Lineup += "\n"

        driver.find_element_by_xpath('//*[@id="lineup_box"]/h3/button').click()

        driver.find_element_by_xpath('//*[@id="home_lineup_btn"]').click()

        Lineup2 += driver.find_element_by_xpath('//*[@id="lineup_box"]/h3').text
        Lineup2 += "\n"
        Lineup2 += "선발투수" + "  " + driver.find_element_by_xpath('//*[@id="lineup_pitcher_player_0"]/td[1]/div/a').text
        Lineup2 += "\n"

        for x in range(0, 9):
            Lineup2 += str(x+1) + "  "
            Lineup2 += driver.find_element_by_xpath('//*[@id="lineup_batter_player_{}"]/td[3]'.format(x)).text
            Lineup2 += "  "
            Lineup2 += driver.find_element_by_xpath('//*[@id="lineup_batter_player_{}"]/td[2]/div/a'.format(x)).text
            Lineup2 += "\n"


        t = twitter()
        t.login()
        t.post(Lineup)
        time.sleep(1)
        t.post(Lineup2)

        # '//*[@id="lineup_batter_player_0"]/td[2]/div/a'
        # '//*[@id="lineup_batter_player_0"]/td[3]'
        #
        # '//*[@id="lineup_batter_player_1"]/td[2]/div/a'

    def sms(self):

        #driver.get('http://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&gameId=20170811SSHH02017')

        driver.get('http://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&data=20170811&gameId=20170811SSHH02017')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        notices = soup.select('#relay_text')

        print(notices)


        # for item in bs.select('span.c_id'):
        #     print(item)
        #
        # l = bs.find_all('div')
        #
        # #print(l)
        #
        # for s in l:
        #     print(s.get('class'))
        #     # try:
        #     #     prop = s.get('class')
        #     #     if prop != None and prop[0] == "scrl_areaovr":
        #     #         l = s
        #     #         print(s)
        #     #         break
        #     # except UnicodeEncodeError:
        #     #     print("Error")

# #access url
# driver.get('https://www.facebook.com')
#
# driver.find_element_by_name('email').send_keys('email')
# driver.find_element_by_name('pass').send_keys('passwd')
#
# driver.find_element_by_id('u_0_u').click()
#
# driver.get('https://www.facebook.com/%ED%95%9C%ED%99%94-%EC%9D%B4%EA%B8%80%EC%8A%A4-%EC%8A%B9%ED%8C%A8-%EC%95%8C%EB%A6%BC-766948450152743/')
#
# try:
#     driver.find_element_by_name('q').send_keys('hi')
#         #driver.find_element_by_xpath('//*[@id="js_8"]/form/div[1]/div[2]/div/textarea').click()
# except:
#     print("fuck")
#
# #driver.find_element_by_class_name('_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft').clic()

if __name__ == '__main__':

    a = getRecord()
    #a.GetLinUp()
    a.sms()