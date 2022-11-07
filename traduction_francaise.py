import random

pierre = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

feuille = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ciseaux = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

jeu_image = [pierre, feuille, ciseaux]

choix_utilisateur = int(input("Qu'est ce que vous choissisez ? Tapez 0 pour Pierre, 1 pour Feuile ou 2 pour Ciseaux. \n"))
print(jeu_image[choix_utilisateur])

choix_ordinnateur = random.randint(0, 2)
print("Le choix de l'ordinnateur:")
print(jeu_image[choix_ordinnateur])

if choix_utilisateur >= 3 or choix_utilisateur < 0: 
  print("Tu as tapé un nombre invalide, tu as perdu !") 
elif choix_utilisateur == 0 and choix_ordinnateur == 2:
  print("Tu as gagné!")
elif choix_ordinnateur == 0 and choix_utilisateur == 2:
  print("Tu as perdu")
elif choix_ordinnateur > choix_utilisateur:
  print("Tu as perdu")
elif choix_utilisateur > choix_ordinnateur:
  print("Tu as gagné!")
elif choix_ordinnateur == choix_utilisateur:
  print("Egalité !")