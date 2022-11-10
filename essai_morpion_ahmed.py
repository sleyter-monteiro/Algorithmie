from random import*
distance=[[1,2,3],[4,5,6],[7,8,9]]
""" Ici dans le n correspond au nombre de ligne que l'on veux 
"""
print("Voici la représentation du cadrillage""\n""A les nombres contenu dans le cadrillage corresponde au case")
print(distance[0])
print(distance[1])
print(distance[2])
grille=("|--|--|--|""\n"
      "|--|--|--|""\n"
      "|--|--|--|")
print("Voici la grille de jeu ")
print(grille)
nom_joueur=input("<< Et toi comment tu t'appelle ? >> ")
def mode_multijoueur(nom_joueur):
      distance = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      print("-----------------BIENVENUE DANS LE MODE MULTIJOUEUR------------------")
      print("Le Joueur 1 est :",nom_joueur)
      nom_joueur_2=input("Merci d'entrer le nom du second joueur.")
      print("Le Joueur 2 est :", nom_joueur_2)
      print("Voici la représentation du cadrillage""\n""A les nombres contenu dans le cadrillage corresponde au case")
      print(distance[0])
      print(distance[1])
      print(distance[2])
      grille = ("|--|--|--|""\n"
                "|--|--|--|""\n"
                "|--|--|--|")
      print("Voici la grille de jeu ")
      print(grille)
      print("")
      print(nom_joueur,"est les X et",nom_joueur_2," les O")
      choix_case = input("Quelle cas tu veux jouer ??")
      if choix_case == "1":
            signe=input("Entre ton signe")
            grille=f'|{signe}|--|--|\n|--|--|--|\n|--|--|--|'
            print(grille)
            choix_case_2 = input("Quelle cas tu veux jouer ??")
            while choix_case_2 == choix_case:
                  choix_case_2 = input("Quelle cas tu veux jouer ??")
            if choix_case_2 == "2":
                  signe_2="O"
                  grille =f'|{signe}||{signe_2}|\n|--|--|--|\n|--|--|--|'
                  print(grille)
                  return grille
                  choix_case=input("Quelle cas tu veux jouer ??")
                  while choix_case == choix_case_2 :
                        choix_case=input("Quelle case tu veux jouer ?? ")


            if choix_case == "3":
                  grille = ("|-x-|--|-O-|"   "\n"
                        "|--|--|--|"   "\n"
                        "|--|--|--|   ")
                  print(grille)
                  return grille
            if choix_case == "4":
                  grille = ("|-x-|--|--|"   "\n"
                        "|-x-|--|--|"   "\n"
                        "|--|--|--|   ")
                  print(grille)
                  return grille
            if choix_case == "5":
                  grille = ("|-x-|--|--|"   "\n"
                        "|--|-x-|--|"   "\n"
                        "|--|--|--|   ")
                  print(grille)
                  return grille
            if choix_case == "6":
                  grille = ("|-x-|--|--|"   "\n"
                        "|--|--|-x-|"   "\n"
                        "|--|--|--|   ")
                  print(grille)
                  return grille
            if choix_case == "7":
                  grille = ("|-x-|--|--|"   "\n"
                              "|--|--|--|"   "\n"
                              "|-x-|--|--|   ")
                  print(grille)
                  return grille

            if choix_case == "8":
                  grille = ("|-x-|--|--|"   "\n"
                              "|--|--|--|"   "\n"
                              "|--|-x-|--|   ")
                  print(grille)
                  return grille

            if choix_case == "9":
                  grille = ("|-x-|--|--|"   "\n"
                              "|--|--|--|"   "\n"
                              "|--|--|-x-|   ")
                  print(grille)


      if choix_case == "2":
            grille=("|--|-x-|--|"   "\n"
                  "|--|--|--|"   "\n"
                  "|--|--|--|   ")
            print(grille)
            return grille

      if choix_case == "3":
            grille=("|--|--|-x-|"   "\n"
                  "|--|--|--|"   "\n"
                  "|--|--|--|   ")
            print(grille)
            return grille
      if choix_case == "4":
            grille=("|--|--|--|"   "\n"
                  "|-x-|--|--|"   "\n"
                  "|--|--|--|   ")
            print(grille)
            return grille
      if choix_case == "5":
            grille=("|--|--|--|"   "\n"
                  "|--|-x-|--|"   "\n"
                  "|--|--|--|   ")
            print(grille)
            return grille
      if choix_case == "6":
            grille=("|--|--|--|"   "\n"
                  "|--|--|-x-|"   "\n"
                  "|--|--|--|   ")
            print(grille)
            return grille
      if choix_case == "7":
            grille=("|--|--|--|"   "\n"
                  "|--|--|--|"   "\n"
                  "|-x-|--|--|   ")
            print(grille)
            return grille

      if choix_case == "8":
            grille=("|--|--|--|"   "\n"
                  "|--|--|--|"   "\n"
                  "|--|-x-|--|   ")
            print(grille)
            return grille

      if choix_case == "9":
            grille=("|--|--|--|"   "\n"
                  "|--|--|--|"   "\n"
                  "|--|--|-x-|   ")
            print(grille)
            return grille

      choix_case_2=input("Quelle cas tu veux jouer ??")

      if choix_case_2 == choix_case:
            print("IMPOSSIBLE")


mode_multijoueur(nom_joueur)