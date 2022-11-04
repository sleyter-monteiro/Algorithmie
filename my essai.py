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
         ontinue
    
    if coupJoueur == "p" :
        print("PIERRE contre ...", end = " ")
    elif coupJoueur == "f" :
        print("FEUILLE contre ...", end = " ")
    else: 
        print("CISEAUX contre ...", end= " ")

    
    randomNombre = random.randint(1,3)
    if randonNombre == 1 :
        coupPC = "p"
        print("PIERRE")
    elif randonNombre == 2 :
        coupPC = "f"
        print("FEUILLE")
    else  :
        coupPC = "c"
        print("CISEAUX")

    if coupJoueur == coupPC :
        print("Match nul!")
        nuls = nuls + 1
    elif coupJoueur == "p" and coupPC == "c" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif coupJoueur == "f" and coupPC == "p" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif coupJoueur == "c" and coupPC == "f" :
        print("Vous avez gagné(e)!")
        user_victoires = user_victoires + 1
    elif coupJoueur == "p" and coupPC == "f" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "f" and coupPC == "c" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "c" and coupPC == "p" :
        print("Vous avez perdu(e)!")
        pc_victoires = pc_victoires + 1
     