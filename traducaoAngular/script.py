from googletrans import Translator
translator = Translator()
import sys
from excecoes import naoTraduzir, traducaoAlternativa

arquivo = ''.join(sys.argv[1])
print ('traduzindo: ', arquivo)

def tiraQuebraLinha(string):
	if string[-1:] == '\n':
		string = string[:-1]
	return string

def tiraEspaco(string):
	espaco = False
	if string[0] ==' ':
		espaco = True
		string = string[1:]
	return espaco, string		

def trocaPalavraEmFrase(string):
    for palavra in traducaoAlternativa:
        if palavra in string:   
            string = string.replace(palavra, traducaoAlternativa[palavra])
    return string
		
def traduzir(string):
	string = translator.translate(string, dest='pt').text
	return string

def validaString(string):
	string = tiraQuebraLinha(string)
	temEspaco, string = tiraEspaco(string)

	if string in traducaoAlternativa:
		string = traducaoAlternativa[string]
	elif '{' in string and len(string) <= 1:
		pass
	elif string not in naoTraduzir:
		string = traduzir(trocaPalavraEmFrase(string))

	if temEspaco:
		string = " " + string

	print(string)
	return string

arq = open(arquivo,'r+')
novo = open(arquivo+'PT','w')

for linha in arq.readlines():
	
	itens = linha.split(':')
	
	if len(itens) <= 1:
		novo.write(''.join(itens))
	else:
		string = ''.join(itens[1:])
		string = validaString(string)
		novo.write(itens[0] + ':' + string + '\n')

	

print ('<<<<<<<<<<<<<<<<<<<<<<<<<<<<Fim!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
