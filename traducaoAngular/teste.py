string = '  "Shelf",'

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
    'Close': 'Fechar'
}

naoTraduzir = ['Rack','  "Shelf",','shelf','Blue Planet']

if string in traducaoAlternativa:
    string = traducaoAlternativa[string]
    print ('traduçãoAlternativa: ', string)
elif string not in naoTraduzir:
    string = 'TRADUZIU'
    #print ('nãoTraduzir: ', string)

print(string)



