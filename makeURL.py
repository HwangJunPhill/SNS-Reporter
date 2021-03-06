from bs4 import BeautifulSoup
import datetime
import urllib.request
import json

def FullURL():
    date = str(datetime.datetime.today().date()).replace('-','')
    key = GetKey()

    if key == "No Game Today":
        return key

    fullUrl = "http://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&data={}&gameId={}{}02017".format(date, date, key)
    return fullUrl

def DataURL():
    date = str(datetime.datetime.today().date()).replace('-','')
    key = GetKey()

    if key == "No Game Today":
        return key

    dataUrl = "http://sportsdata.naver.com/ndata//kbo/2017/08/{}{}02017.nsd".format(date,key)
    return dataUrl

def GetKey():

    urlKey = {}
    req = urllib.request.Request("http://www.hanwhaeagles.co.kr/html/game/1st_schedule_list1.asp")
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')

    for item in bs.select('.box.today'):
        try:
            urlKey['home'] = item.find('em').get_text()

        except:
            #No Game Today
            return "No Game Today"

        else:
            if urlKey['home'] == '':
                urlKey['home'] = "원정경기"
            urlKey['team'] = item.find('img')['alt']

        if urlKey['team'] == "KIA":
            urlKey['team'] = "HT"

        elif urlKey['team'] == "두산":
            urlKey['team'] = "OB"

        elif urlKey['team'] == "KT":
            urlKey['team'] = "KT"

        elif urlKey['team'] == "롯데":
            urlKey['team'] = "LT"

        elif urlKey['team'] == "LG":
            urlKey['team'] = "LG"

        elif urlKey['team'] == "삼성":
            urlKey['team'] = "SS"

        elif urlKey['team'] == "NC":
            urlKey['team'] = "NC"

        elif urlKey['team'] == "SK":
            urlKey['team'] = "SK"

        elif urlKey['team'] == "넥센":
            urlKey['team'] = "WO"

    if urlKey['home'] == "원정경기":
        urlKey['team'] = "HH" + str(urlKey['team'])

    elif urlKey['home'] == "홈경기":
        urlKey['team'] = str(urlKey['team']) +"HH"

    return urlKey['team']

def GetJson(url):

    #req = urllib.request.Request(DataURL())
    #for debug
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()

    data = data.decode(encoding='UTF-8')
    data = urllib.request.unquote(data)

    data = data.replace('<meta http-equiv=Content-type content="text/html; charset=utf-8"><script>document.domain="naver.com";parent.sportscallback_relay(document, ', '')
    data = data.replace(');</script>', '')

    data = json.loads(data)

    return data

    #print(len(data['relayTexts']))


GetKey()

#GetJson()

#print(inputUrlreturnDict())
#If the game set and hh homepaged edited, GetKey only get win or lose.