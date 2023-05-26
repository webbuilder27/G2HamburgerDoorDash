from animal import Animal


class Duck(Animal): 
    livableHabitats = ['Wetland', 'Bathtub']
    
    def __init__(self, species) :
        super().__init__('Duck')
        self.species = species
        self.color = None
        self.Gender = None

    def eat(self): 
        super().eat()

    def die(self): 
        pass

    def walk(self): 
        pass 

    def swim(self): 
        pass

    def speak(self): 
        print('Quack Quack')


    #Notes: 
    #"has a" - > 1. Association (Relationship) 2. Aggregation (I am in control of this object rn) 3.Composition (We cannot live without this)
    #Association & Aggregation (Weak).
    #Composition (Storng)
    #2 directional way Association.  1 directional (Aggregation & Composition)

    # "is a"
    #Inheritance - 
