import  itertools
from builtins import input

caracteres = input("Digite os caracteres a serem permultados: ")
resultado = itertools.permutations(caracteres, len(caracteres))

count = 0
for i in resultado:
    print(''.join(i))
    count=count+1

print(count)

