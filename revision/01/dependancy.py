import sqlite3
import pandas as pd

from consts import *


# CREATION DE LA BASE DE DONNÉES
conn = sqlite3.connect(f"{DB_NAME}.db")

# CREATION DU CURSEUR
cursor = conn.cursor()
