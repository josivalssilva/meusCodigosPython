from hashlib import scrypt
import os

from sympy import resultant

path = '/home/josival/220202_bundles/'

def files_path09(path):
    '''return list of tuple(path, file)'''
    return [(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]


def files_path10(path):
    '''return list of string'''
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]
    

lista = files_path10(path)
tamanho_lista = len(lista)
arquivoRestante = tamanho_lista
print ('Quantidade de arquivos: ',tamanho_lista)

for item in lista:
    restante = 'Faltam: '
    arquivo = ' arquivos'
    
    if arquivoRestante<2:
        restante='Falta: '
        arquivo = 'cle'
    print (restante, arquivoRestante, arquivo)
    os.system('python3 /mnt/Backup/meusCodigosPython/traducaoAngular/script.py '+ item)
    arquivoRestante = arquivoRestante -1
    