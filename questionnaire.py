import json

# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0])
            if self.choix[i][1] == True:
                self.bonne_reponse = self.choix[i][0]

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.bonne_reponse.lower() == self.choix[reponse_int-1][0].lower() :
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self,categorie,titre,difficulte,questions):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte

    def lancer(self):
        print()
        print(f"Bienvenue sur le questionnaire qui porte sur {self.titre}")
        print(f"Catégorie : {self.categorie} | difficulté : {self.difficulte}")
        print(f"nombre total de questions : {len(self.questions)}")
        print()

        score = 0
        for i in range (0,len(self.questions)):
            print(f"Question n° {i+1} / {len(self.questions)}")
            if self.questions[i].poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


# """questionnaire = (
#     ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
#     ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
#     ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
#                 )

# lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

# Questionnaire(
#     (
#     Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
#     Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
#     Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
#     )
# ).lancer()


filename = "arts_museedulouvre_expert.json"
print()

while True:
    propo = input("Voulez vous utiliser un fichier externe (O/N) : " )
    if propo.lower() in ["non","no","n"]:
        break
    if propo.lower() in ["oui","o","yes"]:
        filename = input("Entrez le fichier à utiliser (spécifier le chemin) : ")
        break


data_file = open(f"{filename}","r")
data_file_read = data_file.read()
data_file.close()
data_json = json.loads(data_file_read)
data_question = data_json.get("questions")

# print(data_json["difficulte"])
# print(data_json["categorie"])

# data_question[0]["choix"]


# question = Question("")

# data_question[0]["titre"]

questions = []

for i in range (0,len(data_question)):
    q = Question(data_question[i]["titre"],data_question[i]["choix"])
    questions.append(q)

Questionnaire(data_json["categorie"],data_json["titre"],data_json["difficulte"],questions).lancer()




