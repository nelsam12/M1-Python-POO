#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 09:41:03 2026

@author: nelsam

Récupérer les pays qui se sont qualifiés pour la coupe du monde
"""


# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================
import datetime
from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

# =============================================================================
# CONSTANTES
# =============================================================================
BASE_DIR = Path(__file__).resolve().parent


BASE_URL = "https://en.wikipedia.org/wiki/2025_Africa_Cup_of_Nations"

# USER AGENT NECESSAIRE DANS NOTRE CAS
HEADER = {
    "User-Agent": "TdScrapping/1.0 (contact: kudzo2004@gmail.com)"
}

TABLE_NAME = "pays_qualifies"
# =============================================================================
# SCRAPING DES TEMPERATURES
# =============================================================================

resultats = []

# =============================================================================
# RECUPÉRATION DE LA PAGE
# =============================================================================

response = requests.get(BASE_URL, headers=HEADER)

# print(type(response).text)


soup = BeautifulSoup(response.text, "html.parser")


table = soup.select("table.wikitable.sortable")[0]

trs = table.find_all("tr")
for tr in trs:
    team_tag = tr.find_all('td', align='left')
    if len(team_tag) != 0:
        resultats.append({"team": team_tag[0].find('a').text,
                          "last_updated": datetime.datetime.now()})

# =============================================================================
# TRANSFORMATION EN DATAFRAME
# =============================================================================

df = pd.DataFrame(resultats)
print(df)


# =============================================================================
# CRÉATION DE LA BASE DE DONNÉE ET DE LA CONNEXION
# =============================================================================

conn = sqlite3.connect(f'{BASE_DIR}/coupe_du_monde.db')


# =============================================================================
# VIDER LA BASE DE DONNEES (si je n'utilise pas replace dans df.to_sql)
# =============================================================================

# CURSOR POUR LES REQUÊTES
cur = conn.cursor()


# SUPPRIMER LA TABLE SI ELLE EXISTE

cur.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
conn.commit()

# =============================================================================
# ENREGISTRER DANS LA BASE DE DONNÉES
# =============================================================================

df.to_sql(
    name=TABLE_NAME,
    con=conn,
    if_exists='replace',
    index=False)


print("TERMINEE")


# =============================================================================
# POUR LE LOGS
# =============================================================================


CONTROL_FILE = BASE_DIR / "control.txt"
date = datetime.datetime.now()
with open(CONTROL_FILE, 'a') as f:
    f.write(f"CRON EXECUTÉ AVEC SUCCES À ({date})\n")
