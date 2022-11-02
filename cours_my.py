class MyClass:
    def _init_() :
        self.a = 56

    def my_function() :
        print("coucou")

#def my function()
class_test = MyClass()

class_test_my_function()

variable = class_test.a

class animals :
    def _init_(self, race, name) :
        """
        Fonction d'installisation de la class. Mot clé_init_
        """
        self.race = race
        self.name = name
        self.taille_de_lanimal = self.taille()

        def__taille(self) :
        """
        Fonction privée (__ avant le nom) "taille", renvoyant la taille moyenne de l'animal selon sa race
        """
        if self.race == "axolotl" :
            return(20)
        else :
            return(100)

animals_class_axo = animals("axolotl", "joujou") #Initiation d'une variable avec pour argument passé dans le "_init_" "axolotl" et "joujou"

animals_class_dog = animals("chien","trevor")

animals_class_axo.taille_de_lanimal

animals_class = animals("axolotl","joujou")

animals_class2 = animals("chien" , "trevor")
