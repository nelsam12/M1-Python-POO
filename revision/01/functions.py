# FONCTIONS
from dependancy import *

def enregistrer_client(nom : str, phone: str, cursor = cursor) : 
    query = "INSERT INTO client (nom, phone) VALUES (?,?)"
    cursor.execute(query, (nom, phone))
    
def supprimer_donnees_table(nom_table: str, cursor = cursor):
    cursor.execute("DELETE FROM {}".format(nom_table))

def enregistrer_commande(montant: int, client_id: int , cursor= cursor):
    query = f"INSERT INTO {TABLES_NAMES[1]} (client_id, montant) VALUES (?,?)"
    cursor.execute(query, (client_id,montant))

def get_all_client():
    return get_all(TABLES_NAMES[0])

def get_commande_by_client_id(client_id: int):
    query = f"SELECT * FROM {TABLES_NAMES[1]} WHERE client_id = ?"
    print(query, client_id)
    cursor.execute(query, (client_id,)) 
    return cursor.fetchall()

def get_all_commandes():
    return get_all(TABLES_NAMES[1])

def get_all(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchall()

# CONVERSION VERS UN FICHIER CSV
def convert_to_csv(table_name, columns):
    data = get_all(table_name)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(f'{table_name}.csv',index=False)
    return df