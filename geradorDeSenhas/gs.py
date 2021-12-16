import random
import string

def gerarSenha
tamanho = int(input('Digite o tamanho da senha desejado: '))

chars = string.ascii_letters + string.digits + '!@#$%*()_+{}?:><'

rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for i in range(tamanho)))
