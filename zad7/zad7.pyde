from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod 
    def speak(self):
        super().__init__()
        return 'no sound'
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    def __add__(self, other):
        return self.name + ' i ' + other.name
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Parrot(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('pip', random(50, width-70), random(50, height-50))
        return 'pip'
    

def setup():
    size(400,400)
    textSize(20)
    rex = Dog('Rex')
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik')
    papug = Parrot('Papug')
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, papug]
    print(isinstance(skrypcik, Pet))
    print(rex+benio)
    print(skrypcik+papug)
    
    if isinstance(papug, Pet) == True:
        print "Papug jest petem"
    else:
        print "Papug nie jest petem"
        

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog):
            pet.gimmePaw()

# 1,25pkt głównie brakuje odejmownaia (metoda __sub__ od substract) 
