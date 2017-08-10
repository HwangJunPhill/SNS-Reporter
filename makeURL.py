import time
from bs4 import BeautifulSoup
import datetime
import urllib.request

url = "http://sports.news.naver.com/gameCenter/textRelay.nhn?category=kbo&gameId="

url += str(datetime.datetime.today().date()).replace('-','')

urlKey = {}
req = urllib.request.Request("http://www.hanwhaeagles.co.kr/html/game/1st_schedule_list1.asp")
data = urllib.request.urlopen(req).read()

bs = BeautifulSoup(data, 'html.parser')

for item in bs.select('.box.today'):
    urlKey['home'] = item.find('em').get_text()
    if urlKey['home'] == None:
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
    url += "HH"
    url += str(urlKey['team'])

elif urlKey['home'] == "홈경기":
    url += str(urlKey['team'])
    url += "HH"

url += "2017"

print(url)


#l = bs.find_all('div')
#
# for s in l:
#     try:
#         prop = s.get('class')
#         if prop != None and prop[0] == "box" and len(prop) == 2:
#             l = s
#             break
#     except UnicodeEncodeError:
#         print("Error")
#
#print(l)