import codecs
import sys
import ast

arr = sys.argv[1]
arr = codecs.decode(arr, "hex").decode('utf-8')
arr= arr.split("**")

variables = ast.literal_eval(codecs.decode(sys.argv[2], "hex").decode('utf-8'))

# print(type(variables))
java = {"Declare.inputVar":"","print":"System.out.println"}
cpp = {"Declare.inputVar":"cin<<","print":"cout << ","none":"none"}

languages = {"cpp":cpp,"java":java}

def transcribe(language:str):
 repr = language
 language = languages[language] 
 syntax = []
 scan = None
 for i in arr:
    func,param = i[:i.index("(")] , i[i.index("("):]
    
    if func == "Declare.inputVar":
       scan = True
       try:
         float(param[1:-1])
         if repr == "java":
            syntax.append("= input.nextDouble();")
         elif repr == "cpp":
            syntax.append("cin << " + param)
       except:
         if repr == "java":
            syntax.append(param[2:-2]+" = input.nextDouble()")
         elif repr == "cpp":
            syntax.append("cin >> " + param[2:-2])
             #type String
       continue
    
    elif func == "print":
        syntax.append(language["print"]+param)
 syntax = list(map(lambda elem: elem +"; \n",syntax))
 
 if repr == "java" : 
    syntax.insert(0,'public class Main {\n')
    syntax.insert(1,"public static void main(String[] args) {\n")
    if scan: 
        syntax.insert(1,"import java.util.Scanner;\n")
        syntax.insert(3,"Scanner input = new Scanner(System.in);\n ")
    syntax.append("\t};")
    for identifier,typeof in variables.items():
      if typeof == "num": 
         syntax.insert(3,f"double {identifier};")
         continue
      elif typeof=="string" : 
         syntax.insert(syntax.index("public static void main(String[] args) {\n")+1,f"String  {identifier};\n")
         continue
    
 elif repr == "cpp":
    syntax.insert(0,"#include <stdio.h>\n")
    syntax.insert(1,'using namespace std;\n')
    syntax.insert(2,'int main(){\n')
    
    for identifier,typeof in variables.items():
      if typeof == "num": 
         syntax.insert(3,f"double {identifier};")
         continue
      elif typeof=="string" : 
         syntax.insert(3,f"{typeof} {identifier};")
         continue
    
    syntax.append("return (0);")
     
 syntax.append("}")
 return syntax


print("-----------------Java---------------------")
print()

with open("./Main.java","w") as file:
   for line in transcribe("java"):
    print(line)
    file.write(line)

print()
print("*"*43)
print()
print("------------------CPP----------------------")
print()
with open("./Main.cpp","w") as file:
   for line in transcribe("cpp"):
    print(line)
    file.write(line)
print()
print("*"*43)
