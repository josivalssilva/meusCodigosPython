import os
import socket


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    print("Cliente socket criado com sucesso!!!")

    host = 'localhost'
    porta = 5433
    mensagem = 'Olá servidor, firmeza'

    try:
        s.sendto(mensagem.encode(),(host, 5432))
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()
        print("Cliente: " +dados)
    finally:
        print("Cliente fechando...")
        s.close()

if __name__ == '__main__':
    main()