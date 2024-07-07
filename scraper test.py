import requests
from bs4 import BeautifulSoup

URL = "https://eu.glory4gamers.com/fr/tournois/pc/league-of-legends/2?ajax=1"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
liens = soup.find_all("a",attrs = {'class':'styled-btn bg-blue text-size-big'})

jours = []
for liens in liens:
    lien = liens.get('href', None)
    
    URLE = "https://eu.glory4gamers.com" + lien +"/infos"
    page_secondaire = requests.get(URLE)
    soup_secondaire = BeautifulSoup(page_secondaire.content, 'lxml')
    day = soup_secondaire. find('div', attrs = {'class':'tournament-date-day'})
    jour = day.getText()
    jours.append(jour)


URL_ajax_deux = "https://eu.glory4gamers.com/fr/tournois/pc/league-of-legends/3?ajax=1"
page_ajax_deux = requests.get(URL_ajax_deux)
soup_ajax_deux = BeautifulSoup(page_ajax_deux.content, 'lxml')
liens_ajax_deux = soup_ajax_deux.find_all("a",attrs = {'class':'styled-btn bg-blue text-size-big'})

for liens_ajax_deux in liens_ajax_deux :
    lien_ajax_deux = liens_ajax_deux.get('href')
    URL_secondaire_ajax_deux = "https://eu.glory4gamers.com" + lien_ajax_deux +"/infos"
    page_secondaire = requests.get(URL_secondaire_ajax_deux)
    
    soup_secondaire = BeautifulSoup(page_secondaire.content, 'lxml')
    day = soup_secondaire. find('div', attrs = {'class':'tournament-date-day'})
    jour = day.getText()
    jours.append(jour)


--------------------------------------------------------------------------------------------------------------

from requests import Session

session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('https://eu.glory4gamers.com/fr/tournois/pc/league-of-legends')

response = session.post(
    url='https://eu.glory4gamers.com/fr/tournois/pc/league-of-legends/2?ajax=1',
    data={
        'N': '4294966750',
        'form-trigger': 'moreId',
        'moreId': '156#327',
        'pageType': 'EventClass'
    },
    headers={
        'Referer': 'https://eu.glory4gamers.com/fr/tournois/pc/league-of-legends'
    }
)

print(response.text)
