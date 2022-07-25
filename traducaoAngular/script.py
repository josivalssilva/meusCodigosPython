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
	
		
def traduzir(string):
	string = translator.translate(string, dest='pt').text
	return string

def validaString(string):
	string = tiraQuebraLinha(string)
	temEspaco, string = tiraEspaco(string)

	if string in traducaoAlternativa:
		string = traducaoAlternativa[string]
	elif string not in naoTraduzir:
		
		string = traduzir(string)

	if temEspaco:
		string = " " + string

	print(string)
	return string

arq = open(arquivo,'r+')
novo = open(arquivo+'PT','w')

linhas = []
numeroLinhas = arq.readlines()
for linha in numeroLinhas:
	if linha[0] == '{':
		novo.write('{\n')
	elif linha[0:6] == '    },':
		novo.write('    },\n')
	elif linha[0:5] == '    }':
		novo.write('    }\n')
	elif linha[0] == '}':
		novo.write('}')
	elif linha[0] != '#':
		itens = linha.split(':')
		if len(itens) > 1:
			string = ''.join(itens[1:])
			string = validaString(string)
			linhas.append(string)
			novo.write(itens[0] + ':' + string + '\n')
		else:
			novo.write('\n')
					
	else:
		novo.write(linha)

print ('<<<<<<<<<<<<<<<<<<<<<<<<<<<<Fim!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
