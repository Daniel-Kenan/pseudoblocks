import unittest
# import execution
from os import system as commands
from subprocess import getoutput
import sys
from functions import for_loop
from compile import Compile, Syntax

arguments = sys.argv

class TestCompiler(unittest.TestCase):
    def setUp(self) -> None:

        self.compilation = Compile(filename='unittest',mode = 'r')
        self.compilation.main()
        # self.syntax = Syntax(self.compilation.contents)
        print(self.compilation.contents)
        return super().setUp()
    
    # def test_sum(self):
        # print(command('pseudo'),'')
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)),6 , "Should be 6")
    # def input(self):
        # self.assertRaises(compiler.input_([1,2,3]))
    # def for_loop_syntax():
        # Syntax(['for start = 51 stop = 2 step 200 then','COMMAND','CODS','endfor']).for_loop()


if __name__ == '__main__':
    unittest.main()

