def RegexError(function,match=None):
  
    try :
        return eval(function+"()")
    except: return False

START,STOP = ['start','stop']
PENALTY = u'\u274c '+'Runtime Error:'

class BasicError(Exception):
  f"deals with {START} and {STOP} at the BOF and EOF"
  
  def __init__(self,lines:list):
    self.lines = lines
    self.bof = f'{PENALTY} you did not {START.strip()} the program'
    self.eof = f'{PENALTY} you did not {STOP.strip()} the program'
  
  def __str__(self): 
    if self.lines[0] != START :
         return self.bof
    else: return self.eof