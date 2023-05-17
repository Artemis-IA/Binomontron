import random # Import de la bibliothèque intégrée random
import mysql.connector as mysqlpy # Importdu connecteur SQL necessaire pour interagir avec la base de données (bdd)

# Connexion à la bdd
user = "root"
password = "example"
host = "localhost"
port = "3307"
database = "Binomontron"

bdd = mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)
cursor = bdd.cursor()

query = "SELECT nom, prenom FROM Apprenants;"
cursor.execute(query)

# Récupère les lignes depuis les tables de la bdd appelée, en l'occurence Binomontron
apprenants = cursor.fetchall()
query = "SELECT COUNT(*) FROM Apprenants;"
cursor.execute(query)
nbr_apprenants = cursor.fetchone()[0]
for ligne in cursor:
    print(ligne[0])
    print(ligne[1])

# Mélange aléatoire de la liste des apprenants de la promo
random.shuffle(apprenants)

# Permet de choisir la taille des groupes
print("Il y a", nbr_apprenants,"personnes dans la promo *(o/*")
group_size = int(input("Veuillez saisir la taille du groupe souhaité pour le projet:"))

# Affecte les groupes formés en fonction des critères d'entrée
teams = []
for i in range(0, nbr_apprenants, group_size):
    if i + group_size <= nbr_apprenants:         # Vérifie si le binôme suivant est possible
            teams.append(apprenants[i:i+group_size])  # Ajoute le binôme à la liste des équipes
    if nbr_apprenants + i < nbr_apprenants + 1:       # Vérifie si un apprenant a été exclu du dernier binôme
            last_member = apprenants[-1]      # Récupère le dernier apprenant
            team = random.choice(teams)       # Choix aléatoire d'un binôme existant
            team.append(last_member)          # Ajoute le dernier apprenant au binôme sélectionné

# Affiche les groupes formés
for i, team in enumerate(teams):
    print("Binôme", i + 1,":", " - ".join([f"{prenom} {nom}" for prenom, nom in team]))

# Referme l'accès à la bdd
cursor.close()
bdd.close()


