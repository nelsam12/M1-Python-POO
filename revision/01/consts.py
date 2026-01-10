# CONSTANTES
DB_NAME = "gestion_commerciale"
TABLES_NAMES = ['client', 'commandes', 'client_commandes', 'client_commandes_2']

TABLES_COLUMNS = {
    'client': ['id', 'nom', 'phone'],
    'commandes': ['id', 'client_id', 'montant']
}

# CLIENT

clients = [
    {"nom": "Amadou Diop", "phone": "+221701234567"},
    {"nom": "Fatou Ndiaye", "phone": "+221761112233"},
    {"nom": "Moussa Fall", "phone": "+221781234890"},
    {"nom": "Awa Sow", "phone": "+221771998877"},
    {"nom": "Ibrahima Ba", "phone": "+221701234999"},
    {"nom": "Khady Diallo", "phone": "+221761234321"},
    {"nom": "Cheikh Thiam", "phone": "+221781111222"},
    {"nom": "Mariama Kane", "phone": "+221771234555"},
    {"nom": "Ousmane Sy", "phone": "+221701987654"},
    {"nom": "Ndeye Mbaye", "phone": "+221769876543"}
]