class animals : 
    def __init__(self, race, name) :
        self.race = race
        self.name = name
        self.taille = self.taille()
        
    def taille(self) :
        # fonction privée (__ avant le nom) "taille", renvoyant la taille moyenne de l'aniamal selon sa race
        if self.race == "axolot1" :
            return(20)
        else :
            return(100)   
        
animals_class_axo = animals("axolot1", "joujou")  # Initialisation d'une variable avec pour argument passé dans le "__init__" "axotol1" et "joujou"

animals_class_dog = animals("chien", "trevor") 

animals_class_axo.taille   