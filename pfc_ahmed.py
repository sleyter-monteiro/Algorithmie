# Je teste github pour ahmed

class game():
    def __init__(self):
        self.score_1=0
        self.score_2=0
    def rules(self):
        while self.score_1 or self.score_2 !=3 :
            for i in range(3):
                i=i+1
                choice_pfc_player_1=str(input("Que veux tu jouer"))
                choice_pfc_player_2 =str(input("Que veux tu jouer"))
                if choice_pfc_player_1 == choice_pfc_player_2:
                    self.score_1 += 0
                    self.score_2 += 0
                    print("Personne n'a pas gagné cette manche")
                if choice_pfc_player_1 == "pierre" and choice_pfc_player_2 == "feuille":  # PIERRE VS FEUILLE
                    self.score_2 += 1
                    self.score_1 += 0

                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "pierre" and choice_pfc_player_2 == "ciseaux":  # PIERRE VS CISEAUX
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "feuille" and choice_pfc_player_2 == "pierre":  # FEUILLE VS PIERRE
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "feuille" and choice_pfc_player_2 == "ciseaux":  # FEUILLE VS CISEAUX
                    self.score_2 += 1
                    self.score_1 += 0
                    print("il y'a à la",i,"manche""SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "ciseaux" and choice_pfc_player_2 == "pierre":  # CISEAUX VS PIERRE
                    self.score_2 += 1
                    self.score_1 += 0
                    print("il y'a à la",i,"manche" "SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
                if choice_pfc_player_1 == "ciseaux" and choice_pfc_player_2 == "feuille":  # CISEAUX VS FEUILLE
                    self.score_2 += 0
                    self.score_1 += 1
                    print("il y'a à la",i,"manche" "SCORE BOT =", self.score_2, "SCORE PLAYER =", self.score_1)
pfc=game()
pfc.rules()