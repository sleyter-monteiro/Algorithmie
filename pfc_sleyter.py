import random

def nom_joueur():
    nom = ""
    while nom == "":
        nom = input("Salut, tu t\'apelle comment ? ")
    return nom
 
nom = nom_joueur()  
    
    
joueur_choix = input("Enchanté " + nom + ", Choissisez Pierre, Feuille, Ciseau : ")

def pfc():
    PCwin = 0
    Joueurwin = 0  
    
    PC_list = ["Pierre","Feuille","Ciseau"]
    PC_choice = random.choice(PC_list)
    
    if PC_choice == joueur_choix:
        print("Egalité, aucun point accordé")
        
    elif joueur_choix in ["Pierre","pierre","P","p"]:
        if PC_choice== "Feuille":
            print("PC : j'ai choisi feuille et j'ai gagné :D")
            PCwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))
        if PC_choice == "Ciseau":
            print("PC : j'ai choisi ciseau et j'ai perdu :(")
            joueurwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))
            
    elif joueur_choix in ["Feuille","feuille","F","f"]:
        if PC_choice== "Ciseau":
            print("PC : j'ai choisi ciseau et j'ai gagné :D")
            PCwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))
        if PC_choice == "Pierre":
            print("PC : j'ai choisi pierre et j'ai perdu :(")
            joueurwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))
            
    elif joueur_choix in ["Ciseau","ciseau","C","c"]:
        if PC_choice == "Pierre":
            print("PC : j'ai choisi pierre et j'ai gagné :D")
            PCwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))
        if PC_choice == "Feuille":
            print("PC : j'ai choisi feuille et j'ai perdu :(")
            joueurwin += 1
            print("Score PC" + str(PCwin) + '\n' + "Votre score" + str(Joueurwin))

            
def rejouer():
    reponse = str(input("Tu veux rejouer avec moi ? (O/n): "))
    if reponse == "O":
        joueur_choice = input("Choissisez Pierre, Feuille, Ciseau : ")
    elif reponse != "O":
        exit()

while True:
    pfc()
    rejouer()    