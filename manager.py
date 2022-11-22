import sys
sys.dont_write_bytecode = True
import os
import requests
import urllib.request
import json
from console import console
dir_path = os.path.dirname(os.path.realpath(__file__))

class PackageManager:
     def __init__(self) -> None:
         self.repository = 'https://api.github.com/repos/daniel-kenan/pseudoblocks/contents/Test%20Cases'
         self.packages = os.listdir(f'{dir_path}\\Test Cases')
         self.totalPackages = len(self.packages)
         self.args  = sys.argv[1:]
     
     def main(self):
        args = list(map(lambda x : x.lower().strip(),self.args))
        if not len(args): print('pseu is a testcase manager')
        elif args[0] == "global": self.listglobalCases()
        elif args[0] == "update": self.update()
        elif args[0] == "local" : self.listlocalCases()
        elif args[0] == "download": self.download()
        elif args[0] == "delete" : pass
        else : console('invalid command',color="RED")
     
     def listlocalCases(self):
        console('\nBelow are a list of testcases available on your computer\n\n',color="LIGHTWHITE_EX")
        for key,package in enumerate(self.packages):
            print(key,package,sep=". ")

     def download(self):
        self.update()
        name = sys.argv[1:][1]
        if name == "-recent": pass

        with open(dir_path+'\\library.json','r') as library:
             data = json.load(library)
             url_ = data[f'{name}'] 
             url_ = requests.get(url_)
             files = url_.json()
             package = name
             if name == "-recent" or not os.path.isdir(dir_path+"\\Test Cases\\"+package):
                os.makedirs(dir_path+"\\Test Cases\\"+package)
             
             for file in files :
                name = file['name']
                urldld = file['download_url']
                urllib.request.urlretrieve(urldld,dir_path+'\\Test Cases\\' + package+ '\\'+file['name'])
             console(f"Downloaded {package} testcase",color='GREEN')  
     
     def update(self):
        fetch = requests.get(self.repository)
        packages = fetch.json()
        totalPackages = len(packages)

        with open(dir_path+'\\library.json','w') as library:
            contents = {}
            for package in packages:
                name , url = package['name'], package['url']
                contents[name] = url  
            
            json.dump(contents, library)

     def listglobalCases(self):
      console('\nBelow are a list of testcases available online\n\n',color="LIGHTWHITE_EX")
      fetch = requests.get(self.repository)
      packages = fetch.json()
      
      for number,package in enumerate(packages):
                print(number,package['name'],sep='. ')
               
    

PackageManager().main()

      



