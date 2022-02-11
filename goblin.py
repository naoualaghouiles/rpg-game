import random


class goblin:
    def __init__(self):
        self.__degat = random.randint(2,3)
        self.__loot = random.choice([1,1.5])
        
    @property
    def degat(self):
        """The degat property."""
        return self.__degat
    @degat.setter
    def degat(self, value):
        self.__degat = value
        
    @property
    def loot(self):
        """The loot property."""
        return self.__loot
    @loot.setter
    def loot(self, value):
        self.__loot = value
    
if __name__ == "__main__":
    g=goblin()
    print(g.degat)
    print(g.loot)
    g2=goblin()
    print(g2.degat)
    print(g2.loot)  
      