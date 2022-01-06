-- sqlite3 logement.db
-- .read logement.sql

-- Question 2
-- Commandes de destruction des tables
DROP TABLE IF EXISTS Logement;
DROP TABLE IF EXISTS Facture;
DROP TABLE IF EXISTS Adresse;
DROP TABLE IF EXISTS Ville;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Capteur;
DROP TABLE IF EXISTS Typecapteur;
DROP TABLE IF EXISTS Mesure;

-- Les associations entres les tables
DROP TABLE IF EXISTS Composer;
DROP TABLE IF EXISTS Attacher;
DROP TABLE IF EXISTS Possede;
DROP TABLE IF EXISTS Dedier;
DROP TABLE IF EXISTS Mesurer;

-- Question 3
-- Commandes de creation des tables
-- Le logement qui comporte l'adresse(comme le table etranger), le telephone, l'IP et la date d'insertion.
CREATE TABLE Logement (id INTEGER PRIMARY KEY AUTOINCREMENT, Telephone INTEGER NOT NULL, IP TEXT NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, idAd INTEGER NOT NULL, FOREIGN KEY (idAd) REFERENCES Adresse(id));

-- La facture comporte le type de facture(eau, electricite, dechet etc.), la date d'insertion, le montant et la valeur.
CREATE TABLE Facture (id INTEGER PRIMARY KEY AUTOINCREMENT, TypeFact TEXT NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, Montant INTEGER NOT NULL, Valeur INTEGER NOT NULL);

-- L'adresse est le tableau etranger de logement comporte le nom de la rue, le complement d'adress, le code postale(vient de tableau etranger Code)
CREATE TABLE Adresse (id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Complement TEXT NOT NULL, Code INTEGER NOT NULL, FOREIGN KEY (Code) REFERENCES Ville(Code));

-- La ville comporte le code postal et le nom de la ville et elle est un tableau etranger de l'adresse
CREATE TABLE Ville (Code INTEGER PRIMARY KEY, Nom TEXT NOT NULL);

-- La piece comporte le nom de la piece(Ex:cuisine, salle de bain), les coordonnees en 3 dimensions 
CREATE TABLE Piece (id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, CordX INTEGER NOT NULL, CordY INTEGER NOT NULL, CordZ INTEGER NOT NULL);

-- Le capteur comporte le reference commercial, le reference de la piece, le port de communication, la date d'insertion, le type et la valeur(creer dans les associations)
CREATE TABLE Capteur (id INTEGER PRIMARY KEY AUTOINCREMENT, RefCommerial TEXT NOT NULL, RefPiece TEXT NOT NULL, Port INTEGER NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Le type de capteur comporte l'unite et la plage a precision
CREATE TABLE Typecapteur (id INTEGER PRIMARY KEY AUTOINCREMENT, Unite TEXT NOT NULL, Plage REAL NOT NULL);

-- La mesure de capteur comporte la valeur et la date d'insertion
CREATE TABLE Mesure (id INTEGER PRIMARY KEY AUTOINCREMENT, Valeur INTEGER NOT NULL, DateInsertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Associations
-- Le logement compose des pieces
CREATE TABLE Composer (idLoge INTEGER NOT NULL, idPiece INTEGER NOT NULL, FOREIGN KEY (idLoge) REFERENCES Logement(id), FOREIGN KEY (idPiece) REFERENCES Piece(id), PRIMARY KEY (idLoge, idPiece));

-- Les factures sont attachees au logement
CREATE TABLE Attacher (idFact INTEGER NOT NULL, idLoge INTEGER NOT NULL, FOREIGN KEY (idFact) REFERENCES Facture(id), FOREIGN KEY (idLoge) REFERENCES Logement(id), PRIMARY KEY (idFact, idLoge));

-- Les pieces possedent des capteurs
CREATE TABLE Possede (idPiece INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idPiece) REFERENCES Piece(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY (idPiece, idCap));

-- Le type de capteur est dedie aux capteurs
CREATE TABLE Dedier (idTypecap INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idTypecap) REFERENCES Typecapteur(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY (idTypecap, idCap));

-- La mesure de capteur est le mesurement de capteur
CREATE TABLE Mesurer (idMes INTEGER NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idMes) REFERENCES Mesure(id), FOREIGN KEY (idCap) REFERENCES Capteur(id), PRIMARY KEY(idMes, idCap));

-- Question 4
-- Insertion de donnees
INSERT INTO Logement(Telephone, IP, idAd) VALUES
       (0701020304, "192.168.1.1", 1);
INSERT INTO Adresse (Nom, Complement, Code) VALUES
       ("1 RUE DE JUSSIEU", "BAT A ESCALIER B", 75005),
       ("1 RUE DE JUSSIEU", "BAT B ESCALIER C", 75005);
INSERT INTO Ville (Code, Nom) VALUES
       (75005, "Paris");

INSERT INTO Piece (Nom, CordX, CordY, CordZ) VALUES
       ("cuisine", 10, 20, 30),
       ("bain", 20, 30, 40),
       ("chambre", 30, 40, 50),
       ("salon", 40, 50, 60);

INSERT INTO Composer VALUES (1, 1);
INSERT INTO Composer VALUES (1, 2);
INSERT INTO Composer VALUES (1, 3);
INSERT INTO Composer VALUES (1, 4);

-- Question 5
INSERT INTO Typecapteur (Unite, Plage) VALUES
       ("celsius", 0.5), -- DS18B20
       ("humidite", 2.0), -- DHT22
       ("kg", 0.1), -- HX711
       ("Lux", 0.001); --TSL2591

-- Question 6
INSERT INTO Capteur (RefCommerial, RefPiece, Port) VALUES
       ("DHT22", "bain", 80),
       ("DS18B20", "salon", 80);
INSERT INTO Dedier VALUES (2, 1);
INSERT INTO Dedier VALUES (1, 2);
INSERT INTO Possede VALUES (2, 1);
INSERT INTO Possede VALUES (4, 2);

-- Question 7
INSERT INTO Mesure (Valeur) VALUES
       (20),
       (50);
INSERT INTO Mesurer VALUES (1, 1);
INSERT INTO Mesurer VALUES (2, 2);

-- Question 8
INSERT INTO Facture (TypeFact, DateInsertion, Montant, Valeur) VALUES
       ("Gaz", "2021-10-24 00:00:00",200, 300),
       ("Electricite","2021-10-25 00:00:00", 100, 80),
       ("Eau", "2021-10-26 00:00:00", 50, 500),
       ("Dechet","2021-10-27 00:00:00", 10, 20);
INSERT INTO Attacher VALUES (1, 1);
INSERT INTO Attacher VALUES (2, 1);
INSERT INTO Attacher VALUES (3, 1);
INSERT INTO Attacher VALUES (4, 1);