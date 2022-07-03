#! /usr/bin/python3

import re

COMMENT = "//"
AND = "and"
OR = "or"
RETURN = 'return'

""" type {identifier} = value"""

NUMBER = "num"
STRING = "string"

# class Declare:
    
#     declared_variables = {}
#     def __str__(self) -> str:
#      return f'''
# variable_name : type
# {Declare.declared_variables}'''

#     def register(self):
        
#         if self._type == NUMBER:
#            self.integer()
#         elif self._type == STRING:
#              self.string()
#         else: raise Exception('invalid type')
               
        
#     def __init__(self,line:str):
#         self.command  = line
#         self.line = line.split(" ")
#         self._type = self.line[0]
#         self._identifier = self.line[1]
#         self._value = self.line[-1]
#         Declare.declared_variables[self._identifier] = self._type

#     def integer(self):
#         self._value = float(self._value)
#         globals()[self._identifier] = self._value
#         # print(self._identifier)

    
#     def string(self):
#        if '\"' in self._value or "\'" in self._value:
#         globals()[self._identifier] = self._value
   
#        else : raise Exception('invalid declare')


# a = Declare("string hello = '10'")
# # a = Declare("num helf = 10")
# # a = Declare("string hee = '10'")
# # a = Declare("num hel = 10")
# a.register()

# print(hello)

