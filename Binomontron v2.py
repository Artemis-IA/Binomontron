import random # Import de la bibliothèque intégrée random
import mysql.connector as mysqlpy # Importdu connecteur SQL necessaire pour interagir avec la base de données (bdd)

# Fonction pour se connecter à la bdd
def connect_to_database():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "Binomontron"

    return mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)

# Fonction pour récupérer la liste des apprenants depuis la bdd
def get_apprenants():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT nom, prenom FROM Apprenants;"
    cursor.execute(query)

    apprenants = cursor.fetchall()

    cursor.close()
    connection.close()

    return apprenants

# Fonction pour récupérer le nombre d'apprenants dans la promotion
def get_promo_size():
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT COUNT(*) FROM Apprenants;"
    cursor.execute(query)

    size = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return size

# Fonction pour mélanger aléatoirement la liste des apprenants
def shuffle_apprenants(apprenants):
    random.shuffle(apprenants)

# Fonction pour former les binômes ou groupes en fonction de la taille souhaitée
def make_teams(apprenants, group_size):
    teams = []
    nbr_apprenants = len(apprenants)

    for i in range(0, nbr_apprenants, group_size):
        team = apprenants[i:i+group_size]
        teams.append(team)

    return teams

# Fonction pour afficher les équipes formées
def display_teams(teams):
    for i, team in enumerate(teams):
        print("Binôme", i + 1, ":", team)

# Fonction principale : elle appelle chacune des fonctions définies précedement dans un ordre bien précis
def main():
    apprenants = get_apprenants()
    promo_size = get_promo_size()

    shuffle_apprenants(apprenants)

    group_size = int(input("Veuillez entrer la taille du groupe souhaitée pour le projet: "))

    teams = make_teams(apprenants, group_size)

    display_teams(teams)

# Appel de la fonction principale
main()
