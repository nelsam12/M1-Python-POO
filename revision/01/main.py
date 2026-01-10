from functions import *

# CREATION DES TABLES
# Clients
create_client_table = f"""
    CREATE TABLE IF NOT EXISTS {TABLES_NAMES[0]}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        phone TEXT    
    ); 
"""
cursor.execute(create_client_table)

# Commandes
create_commande_table = f"""
    CREATE TABLE IF NOT EXISTS {TABLES_NAMES[1]}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        montant INT,
        FOREIGN KEY (client_id) REFERENCES client(id)    
    ); 
"""
cursor.execute(create_commande_table)


# INSERTION DES DONNÉES




# SUPPRIMER LES DONNÉES  (client)
supprimer_donnees_table(TABLES_NAMES[0])


# CREATION DES CLIENTS
for client in clients:
    enregistrer_client(client.get("nom"), client.get("phone"))

# RECUPÉRER LES CLIENTS
all_clients = get_all_client()


# CONVERSION VERS UN FICHIER CSV (Client)
client_df = convert_to_csv(TABLES_NAMES[0], columns=TABLES_COLUMNS[TABLES_NAMES[0]])


# SUPPRIMER LES DONNÉES 
supprimer_donnees_table(TABLES_NAMES[1])
# CREATION DES COMMANDES DES CLIENTS
for client in all_clients:
    for i in range(5):
        enregistrer_commande(100 * client[0] * (i+1), client[0])


#  PREMIERE APPROCHE (MANUELLE)
cursor.execute("SELECT nom, SUM(montant) AS total FROM client JOIN commandes ON client.id = commandes.client_id GROUP BY client.id")
results = cursor.fetchall()
client_commandes_df = pd.DataFrame(results, columns=['nom', 'total'])
client_commandes_df.to_sql(TABLES_NAMES[2], conn, if_exists='replace', index=False)

# DEUXIEME APPROCHE (CREER UNE TABLE DANS LA JOINTURE)
create_client_commandes_table = f"""
    CREATE TABLE IF NOT EXISTS {TABLES_NAMES[3]} AS
    SELECT nom , SUM(montant) AS total
    FROM client
    JOIN commandes ON client.id = commandes.client_id
    GROUP BY client.id;
"""

cursor.execute(create_client_commandes_table)

# CONVERSION DES COMMANDES AU FORMAT CSV
commandes_df = convert_to_csv(TABLES_NAMES[1], TABLES_COLUMNS[TABLES_NAMES[1]])

conn.commit() # VALIDATION DES CHANGEMENTS

"""
# CREATION DE LA TABLE CLIENT_COMMANDES
CREATE TABLE IF NOT EXISTS {TABLES_NAMES[2]}(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_complet INTEGER,
    total INT,
);

cursor.execute(create_commande_table)
"""