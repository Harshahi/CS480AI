### Harshavardhan Shahi (hs4728), Madison Miller (mjm1361)
### File Simpsons.py
### Solves problem 1.
                
from search import *

START_POSITION = 0
ACROSS_RIVER = 1

class ObjectPlace(ProblemState):
    """  
    Homer Simpson has to move his daughter Maggie, 
    his dog Santa's Little Helper, and a jar of rat poison 
    that looks like candy across a river. He can only take one 
    item in his boat at a time. He can't leave Maggie alone with 
    the rat poison (or she will eat it) and he can't leave Santa's 
    Little Helper alone with Maggie (because the dog will pester the girl). 
    Formulate the actions for this problem and implement them. 
    Be careful to ensure that illegal states are flagged correctly.
    """
    def __init__(self, homer, maggie, dog, poison):
        self.homer = homer
        self.maggie = maggie
        self.dog = dog
        self.poison = poison
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        positions = ""
        positions += "Homer 1 \n" if self.homer == ACROSS_RIVER else "Homer 0 \n"
        positions += "Maggie 1 \n" if self.maggie == ACROSS_RIVER else "Maggie 0 \n"
        positions += "Santa's Little Helper 1 \n" if self.dog == ACROSS_RIVER else "Santa's Little Helper 0 \n"
        positions += "Jar of rat poison 1 \n" if self.poison == ACROSS_RIVER else "Jar of rat poison 0 \n"
        return positions
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if self.maggie == self.dog and self.dog == self.poison: return 0  #maggie, dog, and poison are in the same location
        if self.maggie == self.dog and self.dog != self.homer: return 1   #maggie and dog are in the same place but not homer
        if self.maggie == self.poison and self.poison != self.homer : return 1  #maggie and poison are in the same place but homer is not

        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return (self.homer == state.homer) and (self.maggie == state.maggie) and (self.dog == state.dog) and (self.poison == state.poison)
    
    def homerAcrossRiver(self):
      return ObjectPlace(ACROSS_RIVER, self.maggie, self.dog, self.poison)

    def homerStartingPos(self):
      return ObjectPlace(START_POSITION, self.maggie, self.dog, self.poison)

    def maggieAcrossRiver(self):
      if self.homer == self.maggie:
        return ObjectPlace(ACROSS_RIVER, ACROSS_RIVER, self.dog, self.poison)
      else: 
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def maggieStartingPos(self):
      if self.homer == self.maggie:
        return ObjectPlace(START_POSITION, START_POSITION, self.dog, self.poison)
      else:
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def dogAcrossRiver(self):
      if self.homer == self.dog:
        return ObjectPlace(ACROSS_RIVER, self.maggie, ACROSS_RIVER, self.poison)
      else:
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def dogStartingPos(self):
      if self.homer == self.dog:
        return ObjectPlace(START_POSITION, self.maggie, START_POSITION, self.poison)
      else:
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def poisonAcrossRiver(self):
      if self.homer == self.poison:
        return ObjectPlace(ACROSS_RIVER, self.maggie, self.dog, ACROSS_RIVER)
      else:
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def poisonStartingPos(self):
      if self.homer == self.poison:
        return ObjectPlace(START_POSITION, self.maggie, self.dog, START_POSITION)
      else:
        return ObjectPlace(self.homer, self.maggie, self.dog, self.poison)
    
    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["homerAcrossRiver", "homerStartPos", 
                "maggieAcrossRiver", "maggieStartPos", 
                "dogAcrossRiver", "dogStartPos",
                "poisonAcrossRiver", "poisonStartPos"]
    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.  
        """
        return [self.homerAcrossRiver(), self.homerStartingPos(), 
                self.maggieAcrossRiver(), self.maggieStartingPos(), 
                self.dogAcrossRiver(), self.dogStartingPos(),
                self.poisonAcrossRiver(), self.poisonStartingPos()]

#Call Search() with initial and final states.
Search(ObjectPlace(START_POSITION, START_POSITION, START_POSITION, START_POSITION), 
        ObjectPlace(ACROSS_RIVER, ACROSS_RIVER, ACROSS_RIVER, ACROSS_RIVER))
