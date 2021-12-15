import os
import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("a conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()

    print("Criado com sucesso!!!")

    host_alvo = input("Difgite o Host a ser conectado: ")

    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente conectado com sucesso no host: " +host_alvo + ", na porta; " +porta_alvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar ao Cliente no host: " + host_alvo + ", na porta; " + porta_alvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()







