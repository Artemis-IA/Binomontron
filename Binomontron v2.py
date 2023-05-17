import random # Import de la bibliothèque intégrée random
import mysql.connector as mysqlpy # Importdu connecteur SQL necessaire pour interagir avec la base de données (bdd)

# Connexion à la bdd
def connect_to_database():
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    database = "Binomontron"

    return mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)

# Récupère la liste des apprenants depuis la bdd
def get_apprenants():
    bdd = connect_to_database()
    cursor = bdd.cursor()

    query = "SELECT nom, prenom FROM Apprenants;"
    cursor.execute(query)

    apprenants = cursor.fetchall()

    cursor.close()
    bdd.close()

    return apprenants

# Mélange aléatoirement la liste des apprenants
def mix_apprenants(apprenants):
    random.shuffle(apprenants)

# Forme les binômes ou groupes en fonction de la taille souhaitée
def make_teams(apprenants, group_size):
    teams = []
    nbr_apprenants = len(apprenants)

    for i in range(0, nbr_apprenants, group_size):
        team = apprenants[i:i+group_size]
        teams.append(team)

    if nbr_apprenants % group_size == 1:
        last_member = teams[-1].pop()  # Retire le dernier apprenant du dernier groupe
        random_group = random.choice(teams[:-1])  # Choix aléatoire d'un groupe existant (hors dernier groupe sinon la groupe est vide)
        random_group.append(last_member)  # Ajoute le dernier apprenant au groupe sélectionné aléatoirement

    return teams

# Afficher les équipes formées
def display_teams(teams):
    for i, team in enumerate(teams):
        if len(team) > 0: # Évite d'afficher un groupe vide
            print("Binôme", i + 1,":", " - ".join([f"{prenom} {nom}" for prenom, nom in team]))
            
# Fonction principale : elle appelle chacune des fonctions définies précedement dans un ordre bien précis
def main():
    apprenants = get_apprenants()
    mix_apprenants(apprenants)
    nbr_apprenants = len(apprenants)
    print("Il y a", nbr_apprenants,"personnes dans la promo *(o/*")
    group_size = int(input("Veuillez entrer la taille du groupe souhaitée pour le projet: "))
    teams = make_teams(apprenants, group_size)
    display_teams(teams)

# Appel de la fonction principale
main()
