import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('./cache/logs.txt','w',encoding='utf-8')

    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    
    def flush(self):pass

sys.stdout = Logger()