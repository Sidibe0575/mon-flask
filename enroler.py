import sqlite3
conn = sqlite3.connect('clients.db')
curseur = conn.cursor()
curseur.execute("""CREATE TABLE IF NOT EXISTS gens(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nom VARCHAR(100) NOT NULL CHECK(length(nom) <=10 ),
   prenom VARCHAR(100) NOT NULL CHECK(length(prenom)  <=10 ),
   numero VARCHAR(16) CHECK(length(numero) <=15 )
   )
   """)
conn.commit()
conn.close()