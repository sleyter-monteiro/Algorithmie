import random
user_choice = input ("Veuillez saisir votre nom : ")
user_victoires = 0
pc_victoires = 0
pc_choice = random.randint(1, 3)
nuls = 0


while True : 
    print(" : " , user_victoires, "égalités : ", nuls, " PC: ", pc_victoires)
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
        
manche_win_user = 0
manche_win_pc = 0
point_user = manche_win_user
point_pc = manche_win_pc        

if user_choice == pc_choice :
        print(f"{point_user} point pour user")
        print(f"{point_pc} point pour pc")
        print("Match nul!")
        point_user += 0
elif user_choice == "p" and pc_choice == "c" :
        print("Vous avez gagné(e)!")
        point_user += 1
elif user_choice == "f" and pc_choice == "p" :
        print("Vous avez gagné(e)!")
        #point_user = user_victoires + 1
        point_user += 1
elif user_choice == "c" and pc_choice == "f" :
        print("Vous avez gagné(e)!")
        point_user += 1
elif user_choice == "p" and pc_choice == "f" :
        print("Vous avez perdu(e)!")
        point_pc += 1
elif user_choice == "f" and pc_choice == "c" :
        print("Vous avez perdu(e)!")
        point_pc += 1
elif user_choice == "c" and pc_choice == "p" :
        print("Vous avez perdu(e)!")
        point_pc += 1
