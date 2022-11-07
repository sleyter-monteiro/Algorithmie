import random
class game():
    def __init__(self):
        self.score_1=0
        self.score_2=0
        self.pierre = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        self.papier = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        self.ciseaux = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

        self.game_images = [self.pierre, self.papier, self.ciseaux]
        self.liste_pfc = ["Pierre","Papier","Ciseaux"]
    def rules(self):
        while self.score_1 or self.score_2 !=3 :   # BOUCLE TANT QUE LE SCORE EST DIFFERENT DE 3 EXECUTER TOUS CEUX QUI YA A L'INTERIEUR DE LA BOUCLE
            for i in range(3): # ICI LA BOUCLE FOR VA NOUS PERMETTRE DE REPETER LA PROGRAMME ET I VA FAIRE OFFICE DE MANCHE
                i=i+1 #ON ATTRIBUT A I LA VALEUR DE 1 POUR QUE LA MANCHE COMMENCE A 1 ET NON PAS 0
                choice_pfc_player_1=str(input("Que veux tu jouer")) #ON DEMANDE AU JOUEUR QU'EST CE QUI VEUT CHOISIR
                choice_pfc_player_2 = random.choice(self.liste_pfc) # LE BOT VA CHOISIR AU HASARD UN CHOIX
                if choice_pfc_player_1 == "Pierre" or "pierre"  : #SI LE CHOIX DU JOUEUR EST PIERRE
                    print(choice_pfc_player_1)
                    """///////"""
                    print(choice_pfc_player_2)
                    print(self.pierre) # ALORS ON AFFICHE LE DESSIN CORRESPONDANT A LA REPONSE
                elif choice_pfc_player_1 == "Papier" or "papier": # SINON SI LE CHOIX DU JOUEUR EST PAPIER
                    print(choice_pfc_player_1)
                    """///////"""
                    print(choice_pfc_player_2)
                    print(self.papier)# ALORS ON AFFICHE LE DESSIN CORRESPONDANT A LA REPONSE
                elif choice_pfc_player_1 == "Ciseaux" or "ciseaux": # SINON SI LE CHOIX DU JOUEUR EST CISEAUX
                    print(choice_pfc_player_1)
                    """///////"""
                    print(choice_pfc_player_2)
                    print(self.ciseaux)# ALORS ON AFFICHE LE DESSIN CORRESPONDANT A LA REPONSE
                else:
                    print("/////////////////////////////////EREUUUUUUR///////////////////")
                if choice_pfc_player_1 == choice_pfc_player_2:
                    self.score_1 += 0
                    self.score_2 += 0
                    print("Personne n'a pas gagné cette manche")
                if choice_pfc_player_1 == "pierre" or "Pierre" and choice_pfc_player_2 == "papier" or "Papier":  # PIERRE VS FEUILLE
                    self.score_2 += 1
                    self.score_1 += 0
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "pierre" or "Pierre" and choice_pfc_player_2 == "ciseaux" or "Ciseaux":  # PIERRE VS CISEAUX
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "papier" or "Papier" and choice_pfc_player_2 == "pierre" or "Pierre":  # PAPIER VS PIERRE
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "papier" or "Papier" and choice_pfc_player_2 == "ciseaux" or "Ciseaux":  # PAPIER VS CISEAUX
                    self.score_2 += 1
                    self.score_1 += 0
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "ciseaux" or "Ciseaux" and choice_pfc_player_2 == "pierre" or "Pierre":  # CISEAUX VS PIERRE
                    self.score_2 += 1
                    self.score_1 += 0
                    print("il y'a à la",i,"manche" "SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "ciseaux" or "Ciseaux" and choice_pfc_player_2 == "papier" or "Papier":  # CISEAUX VS PAPIER
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche" "SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)




pfc=game()
pfc.rules()