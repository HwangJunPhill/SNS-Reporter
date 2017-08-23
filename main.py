from bs4 import BeautifulSoup
import makeURL
from selenium import webdriver
import urllib.request
import time
import blackmagic

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
        self.twit.get('https://twitter.com/')
        self.twit.find_element_by_xpath('//*[@id="global-new-tweet-button"]').click()
        self.twit.find_element_by_xpath('//*[@id="tweet-box-global"]').send_keys(post)
        self.twit.find_element_by_xpath('//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[3]/div[2]/button').click()
        time.sleep(3)

class getRecord:
    def __init__(self):
        self.t = twitter()
        self.t.login()

    def GetLinUp(self):
        url = makeURL.FullURL()
        Lineup = ""
        Lineup2 = ""

        if url == "No Game Today":
            print(url)
            return

        driver.get(url)

        html = driver.page_source

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


        self.t.post(Lineup)
        time.sleep(1)
        self.t.post(Lineup2)

    def sms(self):
        url = makeURL.DataURL()

        if url == "No Game Today":
            print(url)
            return

        tmp = makeURL.GetJson(url)

        curInning = tmp['currentInning']

        curBatter = tmp['relayTexts'][curInning][0]['liveText']

        blackmagic.dbgprint(curInning, curBatter)

        while True:
            data = makeURL.GetJson(url)

            score = data['gameInfo']['hName'] + " " + str(data['scoreBoard']['rheb']['home']['r']) \
                    + " : " + str(data['scoreBoard']['rheb']['away']['r']) + " " + data['gameInfo']['aName']

            string = score

            #if Inning in var curInning and JSON Inning different, refresh and print last liveText
            if curInning != data['currentInning']:
                curInning = data['currentInning']

            #if Current Batter is different with batter in curBatter , print curBatter's record
            #Lead Off
            try:
                if data['relayTexts'][curInning] == []:
                    pass
            except:
                pass

            try:
                if curBatter != data['relayTexts'][curInning][0]['liveText']:
                    curBatterIndex = 0
                    prevBatterIndex = 0

                    for x in data['relayTexts'][curInning]:
                        curBatterIndex += 1
                        if x['liveText'] == curBatter:
                            break

                    for x in range(curBatterIndex, len(data['relayTexts'][curInning])):

                        if data['relayTexts'][curInning][x]['liveText'][1] == '번':
                            prevBatterIndex = x
                            break

                    for x in reversed(range(curBatterIndex, prevBatterIndex)):
                        if data['relayTexts'][curInning][x]['liveText'][1] == '구':
                            pass
                        elif '병살' in data['relayTexts'][curInning][x]['liveText'] \
                                or '주자' in data['relayTexts'][curInning][x]['liveText'] \
                                or '홈인' in data['relayTexts'][curInning][x]['liveText'] \
                                or '홈런' in data['relayTexts'][curInning][x]['liveText'] \
                                or '교체' in data['relayTexts'][curInning][x]['liveText']\
                                or '타격' in data['relayTexts'][curInning][x]['liveText']\
                                or '실패' in data['relayTexts'][curInning][x]['liveText']\
                                or '도루' in data['relayTexts'][curInning][x]['liveText']:

                            string += "\n" + data['relayTexts'][curInning][x]['liveText']

                    curBatter = data['relayTexts'][curInning][0]['liveText']
            except:
                pass

            if string == score:
                pass
            else:

                if data['currentPlayers']['away']['playerType'] == "pitcher":
                    self.pitcher = data['currentPlayers']['away']['playerInfo']['name']
                elif data['currentPlayers']['home']['playerType'] == "pitcher":
                    self.pitcher = data['currentPlayers']['home']['playerInfo']['name']

                string += "\n\n" + "현재 투수 " + self.pitcher

                print(string)
                self.t.post(string)

            string = score

            #if the game set, print final
            if data['relayTexts']['final'] != []:
                for x in data['relayTexts']['final']:
                    string += "\n" + x['liveText']

                print(string)
                self.t.post(string)
                break


if __name__ == '__main__':
    a = getRecord()
    a.GetLinUp()
    a.sms()