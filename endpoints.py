### Imports ###
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
import os

# Download latest database
from utils import download_latest_database
download_latest_database()

db_pfad = os.path.join(os.path.dirname(__file__), "database.db")

# FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datenbank
conn = sqlite3.connect(db_pfad, check_same_thread=False)
cursor = conn.cursor()

### Funktionen ###

# Produkt Name -> Produkt ID
def name_to_id(name):
    cursor.execute("SELECT id FROM Produkte WHERE Name LIKE ?", (f"%{name}%",))
    result = cursor.fetchall() #ID
    if not result:
        return None
    r = [i[0] for i in result]
    return r

# Produkt Barcode -> Proddukt ID
def barcode_to_id(barcode):
    cursor.execute("SELECT id FROM Produkte WHERE Barcode = ?", (barcode,))
    result = cursor.fetchone() #ID
    return result[0] if result else None

# Firmen Name -> Liste der Produkt IDs
def company_to_ids(name):
    cursor.execute("SELECT id FROM Unternehmen WHERE Name LIKE ?", (f"%{name}%",))
    results = cursor.fetchall()
    company_ids = [result[0] for result in results]
    placeholders = ", ".join("?" * len(company_ids))
    cursor.execute(f"SELECT id from Produkte WHERE Unternehmen_ID IN ({placeholders})", company_ids)
    r = [i[0] for i in cursor.fetchall()]
    return r

# ProduktID -> JSON
def get_product(product_id):
    # Produkt
    # Produkt und Unternehmen essenziell
    cursor.execute("SELECT * FROM Produkte WHERE id = ?", (product_id,))
    result_product = cursor.fetchone()
    if not result_product:
        return {}
    
    # Unternehmen    
    cursor.execute("SELECT * FROM Unternehmen WHERE id = ?", (result_product[1],))
    result_unternehmen = cursor.fetchone()
    if not result_unternehmen:
        return {}
    unternehmen = {
        "Name": result_unternehmen[1],
        "Land": result_unternehmen[2],
        "Gründung": result_unternehmen[3],
        "Website": result_unternehmen[4]
    }
    
    # Allergene
    cursor.execute("SELECT Allergen_ID FROM Produkte_Allergene WHERE Produkt_ID = ?", (product_id,))
    result_allergene = cursor.fetchall()
    allergene = []
    for i in result_allergene:
        cursor.execute("SELECT Allergen FROM Allergene WHERE id = ?", (i[0],))
        allergene.append(cursor.fetchone()[0])
    
    # Labels
    cursor.execute("SELECT Label_ID FROM Produkte_Labels WHERE Produkt_ID = ?", (product_id,))
    result_labels = cursor.fetchall()
    labels = []
    for i in result_labels:
        cursor.execute("SELECT Label FROM Labels WHERE id = ?", (i[0],))
        labels.append(cursor.fetchone()[0])
    
    # Bestandteile
    cursor.execute("SELECT Bestandteil_ID FROM Produkte_Bestandteile WHERE Produkt_ID = ?", (product_id,))
    result_bestandteile = cursor.fetchall()
    bestandteile = []
    for i in result_bestandteile:
        cursor.execute("SELECT * FROM Bestandteile WHERE id = ?", (i[0],))
        bestandteil = cursor.fetchone()
        cursor.execute("SELECT * FROM Unternehmen WHERE id = ?", (bestandteil[1],))
        unternehmen_bestandteil = cursor.fetchone()
        _unternehmen_bestandteil = {
            "Name": unternehmen_bestandteil[1],
            "Land": unternehmen_bestandteil[2],
            "Gründung": unternehmen_bestandteil[3],
            "Website": unternehmen_bestandteil[4]
        }
        bestandteile.append({
            "Name": bestandteil[2],
            "Herstellungsort": bestandteil[3],
            "Unternehmen": _unternehmen_bestandteil
        })

    return {
        "Name": result_product[2],
        "Unternehmen": unternehmen,
        "Barcode": result_product[3],
        "Größe": result_product[4],
        "Kategorie": result_product[5],
        "Herstellungsort": result_product[6],
        "Nährwerte": {
            "Brennwert": result_product[7],
            "Fettgehalt": result_product[8],
            "Gesättigte_Fettsäuren": result_product[9],
            "Kohlenhydrate": result_product[10],
            "Zuckergehalt": result_product[11],
            "Eiweißgehalt": result_product[12],
            "Salzgehalt": result_product[13],
        },
        "Labels": labels,
        "Allergene": allergene,
        "Bestandteile": bestandteile
    }

### Endpoints
# Return Produkt JSON with Produkt ID
@app.get("/produkt/id/{id}")
def get_item(id: int):
    return get_product(id)

# Return Produkt JSON with Produkt Barcode
@app.get("/produkt/barcode/{barcode}")
def get_item(barcode: str):
    product_id = barcode_to_id(barcode)
    if not product_id:
        return {}
    return get_product(product_id)

# Return Produkt JSON with Produkt Name
@app.get("/produkt/name/{name}")
def get_item(name: str):
    ids1 = name_to_id(name)
    ids2 = company_to_ids(name)
    if not ids1 and not ids2:
        return {}
    produkte = list(set(ids1+ids2))
    if not produkte:
        return {}
    
    _produkte = []
    for produkt in produkte:
        _produkte.append(get_product(produkt))
    return _produkte

@app.on_event("shutdown")
def shutdown():
    global conn, cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database closed")
