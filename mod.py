import sqlite3
def init_db():
    conne = sqlite3.connect('produits.db')
    curseur = conne.cursor()
    curseur.execute(''' CREATE TABLE IF NOT EXISTS produits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prix TEXT NOT NULL,
    image TEXT NOT NULL
    )
    ''')
    conne.commit()
    conne.close()
def ajouter_produit(nom, prix, image):
    conne = sqlite3.connect('produits.db')
    curseur = conne.cursor()
    curseur.execute('INSERT INTO  produit (nom, prix, image) VALUES ( ?, ?, ?)',(nom, prix, image))
    conne.commit()
    conne.close()
def obtenir_produit():
    conne = sqlite3.connect('produits.db')
    cursor = conne.cursor()
    cursor.execute('SELECT * FROM produits')
    produits = cursor.fetchall()
    conne.close()
    return produits  