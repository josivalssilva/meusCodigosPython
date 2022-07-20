from googletrans import Translator
translator = Translator()

def tiraQuebraLinha(string):
	if string[-1:] == '\n':
		string = string[:-1]
	return string

def removeEspaco(string):
	if string[0:1] == ' ':
		string = string[1:]
	return string

def traduz(string):
	string = translator.translate(string, dest='pt').text
	return string

def validaString(string):
	string = tiraQuebraLinha(string)
	string = removeEspaco(string)
	string = traduz(string)
	return string

arq = open('l10n-messages.properties','r+')
novo = open('output.properties','w')

linhas = []


for linha in arq.readlines():
	if linha[0] != '#': # or linha != '\n':
		itens = linha.split(':')
		if len(itens) > 1:
			string = ''.join(itens[1:])
			string = validaString(string)
			linhas.append(string)
			print(string)
			novo.write(itens[0] + ':' + string + '\n')
	else:
		novo.write(linha + '\n')
		
