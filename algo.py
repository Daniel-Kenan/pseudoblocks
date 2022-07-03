#! /usr/bin/python3

import subprocess
import os
from console import *
import sys
from LogT import *

ENVIROMENT = './playground/'
case_dir = './Test Cases/'
case_filename = sys.argv[1]
path = case_dir + case_filename
pseudocode_file = sys.argv[2]
console(f'\nRUNNING TEST CASE: {case_filename}', 'CYAN')
passed_case = 0
global_payload = []

with open(path + '/brief.txt') as brief:
    print()
    print(brief.readline())

units = os.listdir(case_dir+case_filename)
units.remove('brief.txt')
case_number = iter(range(len(units[:])))
units_length = len(units)
units = iter(units)

print()

def Main():

    def wrapper(task):
      dermacate = f"{'*' * 60}"
      print(dermacate[:27],'Case:' ,next(case_number)+1,dermacate[:26],)
      print()
      task()
      print()
      print("-"*28 + ' DONE ' + "-"*28)
      print('\n')

    @wrapper
    def output():
            global global_payload
            global_payload = []
            with open(path +'/'+next(units)) as payload:
              file_contents = payload.readlines()
              file_contents = list(map(lambda x: x.strip()  , file_contents))
              file_contents = list(filter(lambda x: x != ""  , file_contents))
              EXPECTED_OUTPUT_INDEX = file_contents.index('=> THE EXPECTED SCREEN_OUTPUT SHOULD BE:')
              pass_payload = file_contents[:EXPECTED_OUTPUT_INDEX]
              
              for load in pass_payload:
                if 'num' in load : 
                  global_payload.append( int(load.removeprefix('num').strip()))
                elif 'string' in load: 
                  global_payload.append( load.removeprefix('string').strip())
              
              
              EXPECTED_OUTPUT = file_contents[EXPECTED_OUTPUT_INDEX+1:]
              
              PROGRAM_OUTPUT = str(subprocess.getoutput(f'python compile.py {pseudocode_file} \"{global_payload}\"').strip())

              for line in file_contents[:EXPECTED_OUTPUT_INDEX] :
                print(line)
              print()
              console('THE EXPECTED SCREEN_OUTPUT SHOULD BE:','CYAN')
              print()
              print(EXPECTED_OUTPUT[0])
              print()
              console('PROGRAM GENERATED SCREEN_OUTPUT IS:','CYAN')
              print()
              print(PROGRAM_OUTPUT)
              
              if EXPECTED_OUTPUT[0] == PROGRAM_OUTPUT:
                global passed_case
                passed_case += 1
                print()
                console(u'\u2713'+' passed this case \n','GREEN')
                print()

              else:
                print()
                console(u'\u274c'+' failed this case','RED')
                print()


if __name__  == "__main__" :      
      for unit in range(units_length):
        Main()

      print('From', units_length,'scenario(s), you solved' , passed_case)



