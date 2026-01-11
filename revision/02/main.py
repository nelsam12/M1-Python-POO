#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 23:24:19 2026

@author: nelsam
"""

# =============================================================================
# IMPORTATION DES DEPENDANCES
# =============================================================================
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
from pathlib import Path


# =============================================================================
# CONSTANTES
# =============================================================================
BASE_DIR = Path(__file__).resolve().parent

BASE_URL = 'https://www.worldometers.info'
POPULATION_BY_COUNTRY = f"{BASE_URL}/world-population/population-by-country/"

HEADER = {
    "User-Agent": "RevisionScrapping/1.0 (contact: kudzo2004@gmail.com) / Linux"
}

# =============================================================================
# RECUPERATION DE LA PAGE
# =============================================================================

reponse = requests.get(POPULATION_BY_COUNTRY, headers=HEADER)

# =============================================================================
# PARSER LA PAGE EN HTML EXPLOITABLE
# =============================================================================
soup = BeautifulSoup(reponse.text, "html.parser")

tbody_tag = soup.find('tbody')

trs = tbody_tag.find_all('tr')

# =============================================================================
# TRAITEMENT
# =============================================================================

resultats = []
for tr in trs:
    tds = tr.find_all('td')
    country_tag = tds[1].find('a')
    country = country_tag.text
    country_link = BASE_URL + '/' + country_tag['href']
    population = tds[2].text

    resultats.append({"pays": country,
                      "population": population,
                      "lien": country_link,
                      "last_update": pd.Timestamp.now()
                      })


# =============================================================================
# CONVERSION EN DATAFRAME
# =============================================================================

df = pd.DataFrame(resultats)


# =============================================================================
# CREATION DE LA BASE DONNEES
# =============================================================================

DB_FILE = BASE_DIR / "world.db"
conn = sqlite3.connect(DB_FILE)

# =============================================================================
# ENREGISTERMENT DANS LA BASE DE DONNÉES
# =============================================================================


df.to_sql('world_countries', con=conn, if_exists='replace', index=False)

# =============================================================================
# CONVERSION AU FORMAT CSV
# =============================================================================
CSV_FILE = BASE_DIR / "world_countries.csv"


# =============================================================================
# FICHIER DE CONTRÔLE
# =============================================================================
CONTROL_FILE = BASE_DIR / "control.txt"
with open(CONTROL_FILE, 'a') as f:
    f.write(f"CRON EXÉCUTÉ AVEC SUCCÈS DATE  : {pd.Timestamp.now()}\n")

print("Terminé !")
