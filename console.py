import colorama
colorama.init()

def console(text,color):
    color = 'colorama.Fore.'+color
    print(eval(color),text,sep='',end="")
    print(colorama.Fore.LIGHTWHITE_EX,end='')