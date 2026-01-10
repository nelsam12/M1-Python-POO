#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 00:31:35 2026

@author: nelsam

Le TP consistera à extraire la température de certaines villes depuis ce site 
https://www.timeanddate.com/weather/

- Maroc : Casablanca;  Rabat ; Marrakech ;
- Sénégal : Dakar ; Thies
- Mali : Bamako
- Mauritanie : Nouakchott

"""

# =============================================================================
# IMPORTATION DES DÉPENDANCES
# =============================================================================

import pandas as pd
from bs4 import BeautifulSoup
import requests

# =============================================================================
# CONSTANTES
# =============================================================================

BASE_URL = "https://www.timeanddate.com/weather"


# =============================================================================
# DEFINITION DES VILLES ET URLS
# =============================================================================

villes = {

    "Casablanca (Maroc)": f"{BASE_URL}/morocco/casablanca",
    "Rabat (Maroc)": f"{BASE_URL}/morocco/rabat",
    "Marrakech (Maroc)": f"{BASE_URL}/morocco/marrakech",
    "Dakar (Sénégal)": f"{BASE_URL}/senegal/dakar",
    "Thies (Sénégal)": f"{BASE_URL}/senegal/thies",
    "Bamako (Mali)": f"{BASE_URL}/mali/bamako",
    "Nouakchott (Mauritanie)": f"{BASE_URL}/mauritania/nouakchott"
}


# =============================================================================
# SCRAPING DES TEMPERATURES
# =============================================================================

resultats = []

for ville, url in villes.items():
    response = requests.get(url)

# =============================================================================
#     PARSER EN CODE HTML
# =============================================================================

    soup = BeautifulSoup(response.text, "html.parser")

# =============================================================================
#     EXTRACTION DE LA TEMPERATURE
# =============================================================================

    temp_tag = soup.find("div", class_="h2")
    if temp_tag:
        temperature = temp_tag.text.strip()
    else:
        temperature = "Non disponible"

    resultats.append({
        "Ville": ville,
        "Température": temperature
    })


# =============================================================================
# AFFICHAGE DES RESULTATS
# =============================================================================

df = pd.DataFrame(resultats)
print(df)
