import random
class game():
    def __init__(self):
        self.score_bot=0
        self.score_1=0
        self.liste_pfc = ["pierre","papier","ciseaux"]
    def rules(self):
        while self.score_bot or self.score_1 !=3 :   # BOUCLE TANT QUE LE SCORE EST DIFFERENT DE 3 EXECUTER TOUS CEUX QUI YA A L'INTERIEUR DE LA BOUCLE
            for manche in range(500): # ICI LA BOUCLE FOR VA NOUS PERMETTRE DE REPETER LA PROGRAMME ET I VA FAIRE OFFICE DE MANCHE
                manche = manche+1  #ON ATTRIBUT A I LA VALEUR DE 1 POUR QUE LA MANCHE COMMENCE A 1 ET NON PAS 0
                choice_pfc_player_1=str(input("Que veux tu jouer")) #ON DEMANDE AU JOUEUR QU'EST CE QUI VEUT CHOISIR
                choice_pfc_player_2 = random.choice(self.liste_pfc) # LE BOT VA CHOISIR AU HASARD UN CHOIX
                print(choice_pfc_player_2)
                if choice_pfc_player_1 == choice_pfc_player_2:
                    self.score_1 += 0
                    self.score_bot += 0
                    print("il y'a à la", manche, "manche""SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "pierre" and choice_pfc_player_2 == "papier":  # PIERRE VS FEUILLE
                    self.score_bot += 1
                    self.score_1 += 0
                    print("il y'a à la",manche, "manche""SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "pierre" and choice_pfc_player_2 == "ciseaux":  # PIERRE VS CISEAUX
                    self.score_bot += 0
                    self.score_1 += 1
                    print("il y'a à la",manche,"manche""SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "papier" and choice_pfc_player_2 == "pierre" :  # PAPIER VS PIERRE
                    self.score_bot += 0
                    self.score_1 += 1
                    print("il y'a à la",manche,"manche""SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "papier" or "Papier" and choice_pfc_player_2 == "ciseaux" or "Ciseaux":  # PAPIER VS CISEAUX
                    self.score_bot += 1
                    self.score_1 += 0
                    print("il y'a à la",manche,"manche""SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "ciseaux" or "Ciseaux" and choice_pfc_player_2 == "pierre" or "Pierre":  # CISEAUX VS PIERRE
                    self.score_bot += 1
                    self.score_1 += 0
                    print("il y'a à la",manche,"manche" "SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                elif choice_pfc_player_1 == "ciseaux" or "Ciseaux" and choice_pfc_player_2 == "papier" or "Papier":  # CISEAUX VS PAPIER
                    self.score_bot += 0
                    self.score_1 += 1
                    print("il y'a à la",manche,"manche" "SCORE BOT =", self.score_bot, "SCORE PLAYER =", self.score_1)
                else:
                    print("reuurue")

                print("---------------------------------------------")
pfc=game()
pfc.rules()