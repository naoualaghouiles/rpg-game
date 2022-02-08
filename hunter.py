from msilib.schema import Property
import random
from xml.sax.handler import property_encoding

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
    """The foo property."""
    return self.__degat
@degat.setter
def degat(self, value):
    self.__degat = value
    
@property
def chance(self):
    """The chance property."""
    return self.__chance
@chance.setter
def chance(self, value):
    self.__chance = value
    
@property
def fuite(self):
    """The fuite property."""
    return self.__fuite
@fuite.setter
def fuite(self, value):
    self.__fuite = value
    
@property
def prix(self):
    """The prix property."""
    return self.__prix
@prix.setter
def prix(self, value):
    self.__prix = value
    
@property
def type_unite(self):
    """The type_unite property."""
    return self.__type_unite
# @type_unite.setter
# def type_unite(self, value):
#     self.__type_unite = value