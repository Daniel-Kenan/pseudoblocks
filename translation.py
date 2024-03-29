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
        
    def toJava(self):
        template = Translation.template('java')
        if 'input' in self.contents:
         template.insert(0 ,"import java.util.Scanner;\n\n")
        
         for syntax in range(self.contents):
            if syntax == "string":pass
            

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