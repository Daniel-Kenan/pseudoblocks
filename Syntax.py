import re
from erronoues import RegexError
from tokens import RETURN
from functions import createfunction



class Syntax:
    modulirise = []
    eraser = []    
    
   
    def __init__(self,arr:list):
        self.contents = arr
        self.commands= []
    

    def for_loop(self):
      for key,val in enumerate(self.contents):
        INPUT = r'^for\s+(\w+)\s?=\s?(\d+)\s+stop\s?=\s?(\d+)\s+step\s+(\d+)\s+then'
        match  = re.match(INPUT ,val)
        if match:
             identifier = match.group(1)
             start = match.group(2)
             stop = match.group(3)
             step = match.group(4)
             endindex = self.contents.index('endfor')
             contents = self.contents[key+1:endindex]
            
             self.contents[key] =  f'for_loop({start},{stop},{step},{contents},\'{identifier}\')'
             del self.contents[key+1:endindex+1]
             
        
    def do_while_loop(self):pass

    def if_else(self):
        for key,val in enumerate(self.contents):
             INPUT = r'(^if\s+).* (then)'
             match  = re.match(INPUT ,val)
             if match:
                _syntax = match.group().removeprefix('if').removesuffix('then')
                del self.contents[key]
                endif_index = self.contents.index('endif')
                _temp = self.contents[key:endif_index]
                for string in _temp:
                    if INPUT in r'(^if\s+).* (then)':pass
                

        
    def input(self):
        
        for key,val in enumerate(self.contents):
            INPUT = r'input\s+'
            match  = re.match(INPUT , val,re.I)
            
            if match :
               
                _syntax = re.sub(INPUT,'Declare.inputVar(\'',val,re.I) +f"\')"
                self.contents[key] = _syntax
                # print(_syntax)
    
    def translate(self):
        
        self.input()
        self.output()
        self.for_loop()
        self.while_loop()
        self.do_while_loop()
        self.if_else()
        self.functions()
        self.__eraser()
        
    def while_loop(self):
        for key,val in enumerate(self.contents):
           OUTPUT = r'^while\s'
           match  = re.match(OUTPUT , val,re.I)
        #    print(match)
           if RegexError("match.group",match=match) :
            # condition = val.removeprefix('while').removesuffix('then') 
            syntax = re.sub(OUTPUT,'while_loop("',val,re.I) 
            # exit()
            
            endwhile=self.contents.index('endwhile')
            a = self.contents[key+1:endwhile]
            syntax = re.sub('then',f'",{a})',syntax,re.I) 
            self.contents[key] = syntax

            buffer = self.contents[key:]
            buffer = buffer[::-1]
            position = buffer.index('endwhile') + key
            buffer.remove('endwhile')
            normal = buffer[::-1]
       
            try:
              self.commands = normal[1:]
            except:"no commands detected"
            
            del self.contents[key+1:self.contents.index('endwhile')+1]
            # return self.contents
           
    def functions(self):
       for key,val in enumerate(self.contents):
            OUTPUT = r'^function (\w+)([(].*[)])'
            match  = re.match(OUTPUT , val)
            
            if match:
                _name = match.group(1)
                _arguments = match.group(2)
                _return_index = self.contents[key:].index(RETURN)
                _commands = self.contents[key+1:key+_return_index+1]
                Syntax.modulirise.append(f'createfunction(\'{_name}\',{_commands},\'{_arguments}\')')
                # del self.contents[key:self.contents.index('return')+1]
                Syntax.eraser.append(key)
               
    def __eraser(self):
        
        if len(Syntax.modulirise):
             del self.contents[Syntax.eraser[0]:]

    def output(self):
        for key,val in enumerate(self.contents):
            OUTPUT = r'(^output\s{1,})'
            match  = re.match(OUTPUT , val,re.I)
            if RegexError("match.group",match=match) :
                _syntax = re.sub(OUTPUT,'print(',val,re.I) +f")"
                self.contents[key] = _syntax


# print(Syntax.template(programming_language='c'))

# print(Syntax(['while i != 5 then',['print(a)'],'endwhile']).translate())
# Syntax(['if condition then','if condition then','command','endif']).if_else()
# print(Syntax(['input name']).input())

# a = Syntax(['function myfunc() ','print("angel")','print("hi")','return']).functions()
# print(Syntax.modulirise)
