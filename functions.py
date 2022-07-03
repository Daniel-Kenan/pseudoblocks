from modules import createfunction

def while_loop(condition:str,commands:list):
        condition.split()[0]
        
        boolean_ =exec(condition)
        while boolean_:
             for command in commands:
              exec(command)
              
             boolean_  = eval(condition)

# a = 1
# while_loop('a<4',['print("hello")','a+=2'])
# print(a)

def for_loop(start:int,stop:int,step:int,commands:list,identifier:str="_________"):
    for __i in range(start,stop+1,step):
        exec(f'{identifier}={__i}') 
        
        for command in commands:
            exec(command)


def do_while_loop(condition:str,commands:list):
    for_loop(0,0,1,commands=commands)
    while_loop(condition=condition,commands=commands)


# for_loop(0,5,2,['print("hi")','print("hi")','a=a+1'])
# do_while_loop('a>5',['print("hello")','a+=2'])
def switch(*case):
    __increment = 0
    while __increment < len(case):
        conditions_commands = case[__increment]
        condition = conditions_commands[0]
        commands = conditions_commands[1]
        __increment +=1
        # print(condition,commands)
        if eval(condition):
            for command in commands:
                exec(command)
                __increment = len(case)

# c1 = ['a>4',['print("1")']]
# c2 = ['a==4',['print("2")']]
# c3 = ['a>4',['print("3")']]

# switch(c3,c2,c1)

# # output('"hello"')

# def inputVar(*vars):
    # for var in vars:
        
