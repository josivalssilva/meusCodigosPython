from tokenize import String
from googletrans import Translator
translator = Translator()
import sys, time

arquivo = ''.join(sys.argv[1])
print ('traduzindo: ', arquivo)
espaco = True

def tiraQuebraLinha(string):
	if string[-1:] == '\n':
		string = string[:-1]
		print('2:',string)
	print('3:',string)
	return string

def verificaEspaco(string):
	if string[0:1] ==' ':
		espaco = True
	else:
		espaco = False
	print('5:',string)
	
def traduzir(string):
	espaco = True
	verificaEspaco (string)
	string = translator.translate(string, dest='pt').text
	#time.sleep(0.2)
	if espaco:
		string = ' '+string
	return string

def validaString(string):
	string = tiraQuebraLinha(string)
	
	traducaoAlternativa = {
		'Building': 'Site',
		'a restrições': 'as restrições',
		'Restaurar a padrão': 'Restaurar por padrão',
		'Full Load': 'Carga Máxima',
		'Não consigo logar': 'Não é possível logar',
		'SAML logoutUrl is not configured': 'O URL de saída do SAML não está configurado',
		'Logout': 'Saída',
		'Internal Stack Trace': 'Rastreamento de pilha interno',
		'ReportName': 'Nome do relatório',
		'GLOBAL DEFAULT GRID': 'MODELO DE GRADE PADRÃO GLOBAL',
		'Scratch Pad': 'Caderno de Rascunhos',
		'ScratchPad': 'Caderno de Rascunhos',
		'Widget': 'Ferramenta',
		'widgets': 'ferramentas',
		'name': 'nome',
		'label': 'rótulo',
		'crio': 'criar',
		'No racks': 'Sem racks',
		'"No"': ' "Não"',
		'Status': 'Estado',
		'close': 'fechar', 
		'Close': 'Fechar',
		'"Copy"': ' "Copiar"',
		'"on"': ' "sobre"',
		'"On"': ' "Sobre"',
		'"Control"': ' "Controle"',
		'Close': 'Fechar',
		' "Building",': ' "Site",'
	}

	naoTraduzir = ['Rack',' "Shelf",','Blue Planet',' "Rack",',' "Rack"',' "Blue Planet",',' "Blue Planet"']


	if string in traducaoAlternativa:
		string = traducaoAlternativa[string]
		print ('6:',string)
	elif string not in naoTraduzir:
		string = traduzir(string)
		print ('7:', string)

	print('8:',string)
	

	return string

arq = open(arquivo,'r+')
novo = open(arquivo+'PT','w')

linhas = []

for linha in arq.readlines():
	if linha[0] == '{':
		novo.write('{\n')
	elif linha[0:5] == '    },':
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
			print('10:',string)
			novo.write(itens[0] + ':' + string + '\n')
		else:
			novo.write('\n')
	else:
		novo.write(linha)

print ('<<<<<<<<<<<<<<<<<<<<<<<<<<<<Fim!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
