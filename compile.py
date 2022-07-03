#! /usr/bin/python3
from Syntax import Syntax
import sys
from erronoues import *
from tokens import *
from Logger import *
from functions import *

__testcase__ = False
arguments = sys.argv

if len(arguments) > 2: 
     test_payload = eval(arguments[2])
     payload=iter(test_payload)
     __testcase__ = True

class Declare:
    
    declared_variables = {}
    def __str__(self) -> str:
     return f'''
variable_name : type
{Declare.declared_variables}'''

    def register(self):
        
        if self._type == NUMBER:
           self.integer()
        elif self._type == STRING:
             self.string()
        else: raise Exception('invalid type')
               
        
    def __init__(self,line:str):
        self.command  = line
        self.line = line.split(" ")
        self._type = self.line[0]
        self._identifier = self.line[1]
        self._value = self.line[-1]
        Declare.declared_variables[self._identifier] = self._type
    
    @staticmethod
    def inputVar(identifiers:str):
        if ',' in identifiers:
            identifiers = identifiers.split(',')
        else : identifiers = [identifiers]
        for identifier in identifiers:
            _type = Declare.declared_variables[identifier]
            if _type == NUMBER:
                if not __testcase__:globals()[identifier] = float(input())
                else : globals()[identifier] = next(payload) 
            else:
                if not __testcase__:globals()[identifier] = input()
                else : globals()[identifier] = next(payload)


    def integer(self):
        self._value = float(self._value)
        globals()[self._identifier] = self._value
        # print(self._identifier)

    
    def string(self):
       if '\"' in self._value or "\'" in self._value:
        globals()[self._identifier] = self._value
   
       else : raise Exception('invalid declare')


class Compile:
    
    def __init__(self,filename,mode='r') -> None:
        self.filename = filename
        self.filepath = f'./playground/{self.filename}'
        self.mode = mode
        with open(self.filepath,self.mode) as algorithm:
            self.contents = algorithm.readlines()
            self.contents = list(map(lambda line: line.strip(), self.contents))
            self.contents = list(filter(lambda line: len(line)>0 and COMMENT not in line, self.contents))
            
    def bof_to_eof(self):
        if START in self.contents and STOP in self.contents:
        #    self.contents = self.contents[self.contents.index(START)+1:self.contents.index(STOP)]
           self.contents.remove(START)
           self.contents.remove(STOP)
        elif not len(self.contents) > 0 : exit()
        else :  raise BasicError(self.contents)
    
    def main(self):
        self.initterm()
        self.bof_to_eof()
        self.observe()
    
    def initterm(self):
        if len(self.contents) > 0 and not (START == self.contents[0]):
            raise BasicError('incorrect way of starting the program')

    def observe(self):
        if START in self.contents: raise Exception(START)
        if STOP in self.contents: raise Exception(STOP)
        
def while_loop(condition:str,commands:list):
        
        boolean_ =eval(condition)
        while boolean_:
             for command in commands:
              exec(command)
              
             boolean_  = eval(condition)


if __name__ == "__main__":

    compilation = Compile(filename = arguments[1])
    compilation.main()
    syntax = Syntax(compilation.contents)
    # print(syntax.contents)
    syntax.translate()
    # print(Syntax.modulirise)
    # print(syntax.contents)
    # exit()
# syntax.while_loop("i != 5 ",9)
    for line in syntax.modulirise:
        exec(eval(line))
 
    if "Declarations" in syntax.contents:
        index_declaration = syntax.contents.index("Declarations")
        syntax.contents.remove("Declarations")
        line = syntax.contents[index_declaration]
        while  line.startswith('num') or line.startswith('string'):
            del syntax.contents[index_declaration]
            if "=" in line:Declare(line).register()
            else: Declare(line) 
            line = syntax.contents[index_declaration]
    
    
    for line in syntax.contents:
        # print(line)
        exec(line)
   