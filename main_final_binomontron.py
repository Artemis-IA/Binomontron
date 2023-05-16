import random
import mysql.connector as mysqlpy

user = "root"
password = "example"
host = "localhost"
port = "3307"
database = "Binomontron"

bdd = mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)
cursor = bdd.cursor()

query = "SELECT nom, prenom FROM Apprenants;"
cursor.execute(query)
promo_ia = cursor.fetchall()
query = "SELECT COUNT(*) FROM Apprenants;"
cursor.execute(query)

def binomontron():
    size = cursor.fetchone()[0] 
    teams = []

    random.shuffle(promo_ia)
  
    # Vérifier si la taille de la promo est impaire et ajuster le pas et la taille si nécessaire
    if size % 2 != 0:
        step = 2
        size += 1
    else:
        step = 2

    # Créer les équipes de 2 personnes
    for i in range(0, size, step):   
        if i + step <= size:
            teams.append(promo_ia[i:i+step])        

    # Gérer le dernier binôme avec 3 personnes si nécessaire
    if len(teams[-1]) == 1:
        last_member = teams.pop()
        random.choice(teams).append(last_member[0])

    # Afficher les équipes
    for i, team in enumerate(teams):
        print("Binôme", i + 1, ":", team)

binomontron()
cursor.close()
bdd.close()
