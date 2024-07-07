import requests
from bs4 import BeautifulSoup

URL = "https://eu.glory4gamers.com/fr/jeu/pc/league-of-legends"



page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

heure=[]
Nom=[]
Mode_de_jeu=[]
Type=[]
Entree=[]
Récompense=[]
PrizePool=[]
Lien=[]
jours = []

liens = soup.find_all("a",attrs = {'class':'styled-btn bg-blue text-size-big'})
for liens in liens:
    lien = liens.get('href', None)
    URLE = "https://eu.glory4gamers.com" + lien +"/infos"
    page_secondaire = requests.get(URLE)
    soup_secondaire = BeautifulSoup(page_secondaire.content, 'lxml')
    day = soup_secondaire. find('div', attrs = {'class':'tournament-date-day'})
    jour = day.getText()
    jours.append(jour)




# Ici test dictionnaire concluant  
test_boi = {
       "Days" : ['18', '19', '20'],
       "Entreee" : ['payante', 'payante', 'payante'],
       "Nomss" : ['Extraordinaire', 'waow', 'incroyable']
        }
test_boi.update(Days = jours)


#transformation test de dictionnaire à dataframe

blui = ['a','b','c']
pip install pandas
import pandas as pd
pd.DataFrame([test_boi])

df = pd.DataFrame.from_dict(test_boi)

#Change l'output l'index devient une colonne
df.set_index('Nomss')

