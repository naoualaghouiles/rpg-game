
import random


class hunter:


  # instance attribute
    def __init__(self):
      self.__degat = random.randint(1,2)
      self.__chance=10
      self.__fuite=20
      self.__prix=25
      self.__type_unite="hunter"
    
    @property
    def degat(self):
      return self.__degat
    
    @degat.setter
    def degat(self, value):
      self.__degat = value
      
    @property
    def chance(self):
        return self.__chance
      
    @chance.setter
    def chance(self, value):
        self.__chance = value
        
    @property
    def fuite(self):
      return self.__fuite
    
    @fuite.setter
    def fuite(self, value):
      self.__fuite = value
    
    @property
    def prix(self):
    
      return self.__prix
    
    @prix.setter
    def prix(self, value):
      self.__prix = value
    
    @property
    def type_unite(self):
    
      return self.__type_unite
  
    @type_unite.setter
    def type_unite(self, value):
      self.__type_unite = value


if __name__ == "__main__":
    
    h = hunter()
    print(h.degat)
    hh= hunter()
    hh.degat=2
    print(hh.degat) 