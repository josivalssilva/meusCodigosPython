import  hashlib

texto = input("Digite o texto a ser gerado a hach: ")

menu = int(input('''### MENU - ESCOLHA O TIUPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print('O hash da String MD5 é: ', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print('O hash da String SHA1 é: ', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print('O hash da String SHA256 é: ', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print('O hash da String SHA512 é: ', resultado.hexdigest())

else:
    print("Algo errado não deu certo, kkk")