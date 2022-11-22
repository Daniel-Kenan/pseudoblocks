from Syntax import Syntax

templateDir = './pseudo-blocks/templates/Main.'

class Translation:
    def __init__(self,syntax:list) -> None:
         self.contents = syntax
    
    
    def __str__(self) -> str:
       return "".join(self.contents)
    
    @staticmethod 
    def template(programming_language):
        with open(templateDir+programming_language) as template:
            contents = template.readlines()
            return contents
    
    def gen(self):
        for i in range(10000):
            yield i
    
    def increment(self):next(self.gen())
        
    def toJava(self):
        template = Translation.template('java')
        if 'input' in self.contents:
         template.insert(self.increment() ,"import java.util.Scanner;\n\n")
        
         for i in range(self.contents):
            if i == "string":pass
            

            # template.insert(4,"\t Scanner input = new Scanner(System.in);")
        java_syntax = template
        self.contents = java_syntax
          
    

    @property
    def toC(self):
        template = Translation.template('c')
        
syntax = Syntax([])

translate = Translation(syntax.contents)
template = Translation.template('java')
translate.toJava() 
print(translate)