from hashlib import scrypt
import os

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
    print ('Restam:', arquivoRestante, ' arquivos')
    # print ('python3 /mnt/Backup/meusCodigosPython/traducaoAngular/scrypt.py '+ item)
    os.system('python3 /mnt/Backup/meusCodigosPython/traducaoAngular/script.py '+ item)
    arquivoRestante = arquivoRestante -1


