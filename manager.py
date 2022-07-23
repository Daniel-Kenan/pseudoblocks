import os
import sys
import requests
import urllib.request
import json
from console import console

class PackageManager:
     def __init__(self) -> None:
         self.repository = 'https://api.github.com/repos/daniel-kenan/pseudoblocks/contents/Test%20Cases'
         self.packages = os.listdir(f'{sys.path[3]}\\Test Cases')
         self.totalPackages = len(self.packages)
         self.args  = sys.argv[1:]
     
     def main(self):
        args = list(map(lambda x : x.lower().strip(),self.args))
        if not len(args): print('pseu is a testcase manager')
        elif args[0] == "update": self.update()
        elif args[0] == "tests" : self.listlocalCases()
        elif args[0] == "download": self.download()
        elif args[0] == "delete" : pass
     
     def listlocalCases(self):
        print()
        for i in self.packages:
            print("",i)

     def download(self):
        self.update()
        name = sys.argv[1:][1]
        if name == "-recent": pass

        with open(sys.path[3]+'\\library.json','r') as library:
             data = json.load(library)
             url_ = data[f'{name}'] 
             url_ = requests.get(url_)
             files = url_.json()
             package = name
             if name == "-recent" :
                os.makedirs(sys.path[3]+"\\Test Cases\\"+package)
             for file in files :
                name = file['name']
                urldld = file['download_url']
                urllib.request.urlretrieve(urldld,sys.path[3]+'\\Test Cases\\' + package+ '\\'+name)
             console(f"Downloaded {package} testcase",color='GREEN')  
     def update(self):
        fetch = requests.get(self.repository)
        packages = fetch.json()
        totalPackages = len(packages)

        with open(sys.path[3]+'\\library.json','w') as library:
            contents = {}
            for package in packages:
                name , url = package['name'], package['url']
                contents[name] = url  
            
            json.dump(contents, library)


PackageManager().main()

      



