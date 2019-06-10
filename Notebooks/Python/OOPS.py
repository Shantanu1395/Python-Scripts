from datetime import date 
import abc

class AgeComponent(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def showAge(self):
    pass

class Dog(AgeComponent):
  """This docstring contains info about Dog."""
  species = 'mammal'

  def __init__(self, name = None, age = None):
        if(name is not None and age is not None):
          self.name = name
          self.age = age
        else:
          self.name = "Default"
          self.age = 2  
  
  #Instance methods
  def makeNoise(self):
    """This is the function docstring."""
    print(self.name +" is barking.")     

  #Creating factories
  @classmethod
  def fromBirthYear(cls, name, year): 
    return cls(name, date.today().year - year)  

  @staticmethod
  def isAdult(age): 
    return age > 5  

  @staticmethod
  def isMammal():
    return Dog.species == 'mammal'    

  #Implementing interface method
  def showAge(self):
    print("Dog age is " + str(self.age))

  #Dunders
  def __repr__(self):
    return 'Object: {}'.format(self.age)    

  def __add__(self, other):
    return self.age + int(other)

  def __len__(self):
    return len(self.name)  

  def __eq__(self, other):
    return self.age == other.age and self.name == other.name

  def __hash__(self):
    print('The hash is:')
    return hash((self.age, self.name))
    

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs at {} kmph".format(self.name, speed)

d = Dog("Rocky", 4)
print(d.name, d.age, d.species)
print(d.__class__.species)
dog = Dog.fromBirthYear('Tim', 1996)
print("Dog from birthYear") 
print(dog.name, dog.age)
print("Is adult: " + str(Dog.isAdult(22)))
print()
print("Is mammal: " + str(dog.isMammal()))
print()
dog.showAge()

d = Dog()
print(d.name, d.age, d.species)

jim = Bulldog("Jim", 12)
print(jim.makeNoise())
print(jim.run(5))
print("Is instance :" + str(isinstance(jim, Dog)))

#Dunders
print(d)
print(d + 3)
print("Length: "+str(len(d)))
print("Hash: "+ str(hash(d)))

#<	object.__lt__(self, other)
#<=	object.__le__(self, other)
#==	object.__eq__(self, other)
#!=	object.__ne__(self, other)
#>=	object.__ge__(self, other)
#>	object.__gt__(self, other)

#+	object.__add__(self, other)
#-	object.__sub__(self, other)
#*	object.__mul__(self, other)
#//	object.__floordiv__(self, other)
#/	object.__truediv__(self, other)
#%	object.__mod__(self, other)

#-	object.__neg__(self)
#+	object.__pos__(self)
#abs()	object.__abs__(self)
#~	object.__invert__(self)
#complex()	object.__complex__(self)
#int()	object.__int__(self)
#long()	object.__long__(self)
#float()	object.__float__(self)
#oct()	object.__oct__(self)
#hex()	object.__hex__(self


#getattr(), setattr(), delattr(obj, name), hasattr(obj, name)
print(getattr(d, 'name'))

setattr(d, 'name', 'Jenny')
print(d.name)

delattr(d, 'name')
if(hasattr(d, 'name')):
  print(d.name)


#__dict__, __doc__ - Prints info about docstring, __module__ - info about which module contains class
print(d.__doc__)  
print(d.makeNoise.__doc__)
print(d.__dict__)  
print(d.__module__)  
