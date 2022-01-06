import sqlite3, random
def drop_db(db_path):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('DROP TABLE IF EXISTS Logement')
    cursor.execute('DROP TABLE IF EXISTS Facture')
    cursor.execute('DROP TABLE IF EXISTS Adresse')
    cursor.execute('DROP TABLE IF EXISTS Ville')
    cursor.execute('DROP TABLE IF EXISTS Piece')
    cursor.execute('DROP TABLE IF EXISTS Capteur')
    cursor.execute('DROP TABLE IF EXISTS Typecapteur')
    cursor.execute('DROP TABLE IF EXISTS Mesure')
    cursor.execute('DROP TABLE IF EXISTS Composer')
    cursor.execute('DROP TABLE IF EXISTS Attacher')
    cursor.execute('DROP TABLE IF EXISTS Possede')
    cursor.execute('DROP TABLE IF EXISTS Dedier')
    cursor.execute('DROP TABLE IF EXISTS Mesurer')
    connect.commit()
    
def creat_db(db_path):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE Logement (id INTEGER PRIMARY KEY AUTOINCREMENT, Telephone INTEGER NOT NULL, IP TEXT NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, idAd INTEGER NOT NULL, FOREIGN KEY (idAd) REFERENCES Adresse(id))')
    cursor.execute('CREATE TABLE Facture (id INTEGER PRIMARY KEY AUTOINCREMENT, TypeFact TEXT NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, Montant INTEGER NOT NULL, Valeur INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE Adresse (id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Complement TEXT NOT NULL, Code INTEGER NOT NULL, FOREIGN KEY (Code) REFERENCES Ville(Code))')
    cursor.execute('CREATE TABLE Ville (Code INTEGER PRIMARY KEY, Nom TEXT NOT NULL)')
    cursor.execute('CREATE TABLE Piece (id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, CordX INTEGER NOT NULL, CordY INTEGER NOT NULL, CordZ INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE Capteur (id INTEGER PRIMARY KEY AUTOINCREMENT, RefCommerial TEXT NOT NULL, RefPiece TEXT NOT NULL, Port INTEGER NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('CREATE TABLE Typecapteur (id INTEGER PRIMARY KEY AUTOINCREMENT, Unite TEXT NOT NULL, Plage REAL NOT NULL)')
    cursor.execute('CREATE TABLE Mesure (id INTEGER PRIMARY KEY AUTOINCREMENT, Valeur INTEGER NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    cursor.execute('CREATE TABLE Composer (idLoge INTEGER NOT NULL, idPiece INTEGER NOT NULL, FOREIGN KEY (idLoge) REFERENCES Logement(id), FOREIGN KEY (idPiece) REFERENCES Piece(id), PRIMARY KEY (idLoge, idPiece))')
    cursor.execute('CREATE TABLE Attacher (idFact INTEGER NOT NULL, idLoge INTEGER NOT NULL, FOREIGN KEY (idFact) REFERENCES Facture(id), FOREIGN KEY (idLoge) REFERENCES Logement(id), PRIMARY KEY (idFact, idLoge))')
    cursor.execute('CREATE TABLE Possede (idPiece INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idPiece) REFERENCES Piece(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY (idPiece, idCap))')
    cursor.execute('CREATE TABLE Dedier (idTypecap INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idTypecap) REFERENCES Typecapteur(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY (idTypecap, idCap))')
    cursor.execute('CREATE TABLE Mesurer (idMes INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idMes) REFERENCES Mesure(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY(idMes, idCap));')
    connect.commit()
# ouverture/initialisation de la base de donnee 

conn = sqlite3.connect('logement.db')
drop_db('logement.db')
creat_db('logement.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

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
