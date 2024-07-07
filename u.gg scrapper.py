import requests
from bs4 import BeautifulSoup
url = "https://euw.op.gg/summoner/matches/ajax/averageAndList/startInfo=0&summonerId=24157549&type=soloranked"
page = requests.get(url)

import json
json = json.loads(page.content)

soup = BeautifulSoup(json['html'], 'lxml')

kda = soup.find("div",attrs = {'class':'Summoner'})
print(kda)