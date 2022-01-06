import sqlite3, random

# ouverture/initialisation de la base de donnee 
conn = sqlite3.connect('logement.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# A completer...

# Afficher les logements
for raw in c.execute('SELECT * FROM Logement'):
    print(raw.keys())
    print(raw["Telephone"])
    print(raw["IP"])
    print(raw["DateInsertion"])
    print(raw["idAd"])

# insertion d'une donnee
c.execute("INSERT INTO Facture (TypeFact, DateInsertion, Montant, Valeur) VALUES ('Gaz', '2021-10-28 00:00:00',500, 500);")
c.execute("INSERT INTO Attacher VALUES (5, 1);")

c.execute("INSERT INTO Facture (TypeFact, DateInsertion, Montant, Valeur) VALUES ('Electricite', '2021-10-29 00:00:00',600, 600);")
c.execute("INSERT INTO Attacher VALUES (6, 1);")

c.execute("INSERT INTO Facture (TypeFact, DateInsertion, Montant, Valeur) VALUES ('Dechet', '2021-10-30 00:00:00',200, 200);")
c.execute("INSERT INTO Attacher VALUES (7, 1);")

# Afficher les factures
for raw in c.execute('SELECT * FROM Facture'):
    print(raw.keys())
    print("Le type de facture est: " + raw["TypeFact"])
    print("La date est: " + raw["DateInsertion"])
    print("Le montant est: " + str(raw["Montant"]))
    print("La valeur est: " + str(raw["Valeur"]))
    
# fermeture
conn.commit()
conn.close()
