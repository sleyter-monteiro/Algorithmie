rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])









import random
nom = input ("Veuillez saisir votre nom : ")
user_victoires = 0
pc_victoires = 0
nuls = 0

while True : 
    print(nom, " : " , user_victoires, "égalités : ", nuls, " PC: ", pc_victoires)
    coupJoueur = input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter.")
    if coupJoueur == "q" :
         print("Vous avez quittez le jeu.")
         break
    if coupJoueur != "p" and coupJoueur != "f" and coupJoueur != "c" :
         continue
    
    if user_choice == "p" :
        print("PIERRE contre ...", end = " ")
    elif user_choice == "f" :
        print("FEUILLE contre ...", end = " ")
    else: 
        print("CISEAUX contre ...", end= " ")

    
    randomNombre = random.randint(1,3)
    if randomNombre == 1 :
        coupPC = "p"
        print("PIERRE")
    elif randomNombre == 2 :
        coupPC = "f"
        print("FEUILLE")
    else :
        coupPC = "c"
        print("CISEAUX")

    if user_choice == pc_choice :
        print("Match nul!")
        nuls = nuls + 1
    elif user_choice == "p" and pc_choice == "c" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif user_choice == "f" and pc_choice == "p" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif user_choice == "c" and pc_choice == "f" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif user_choice == "p" and pc_choice == "f" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1
    elif user_choice == "f" and pc_choice == "c" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1
    elif user_choice == "c" and pc_choice == "p" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1