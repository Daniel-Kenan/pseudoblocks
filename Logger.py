import sys
import os

__pseudodirname__ = '__plogs__'

if not os.path.isdir(__pseudodirname__):
    os.makedirs(__pseudodirname__)

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('./'+__pseudodirname__+'/ProgramOutput.txt','w',encoding='utf-8')

    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    
    def flush(self):pass

sys.stdout = Logger()