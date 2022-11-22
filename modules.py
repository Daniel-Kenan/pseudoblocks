from tokens import RETURN

def createfunction(name,commands:list=[],args:str = '()'):
    indentation = "\n \t"
    func = [f'def {name}{args}:']

    for command in commands:
      func.append(command)
    # func.append(RETURN)

    define = indentation.join(func)
    code = compile(define,'function','exec')
    return code

if __name__ == "__main__":
    a = ['a','b','c']
    for i in a:
        exec(createfunction(i,[]))

    a()
    b()
    c()
    # exec(createfunction('j'))

