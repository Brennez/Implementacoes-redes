from ast import Try
from http import client
import socket
from urllib import request, response

HOST = 'localhost'
PORT = 8081

# Criando socket com IPV4 (AF_INET) usando conexão TCP(SOCK_STREAM)
socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Permite reusar a porta e o endereço do server caso seja encerrado incorretamente
# socket.setsockopt(socket.SOCKET_SOCKET, socket.SO_REUSEADDR, 1)

# Faz a junção (bind) do servidor com a porta
socket.bind((HOST, PORT))

# fica escutando requisições na porta especificada
socket.listen(PORT)

print("Servidor rodando na porta {}".format(PORT))

while True:
    # Aguarda por novas conexões
    client_conection, client_addres = socket.accept()
    # O método .recv recebe os dados enviados por um cliente através do socket
    request = client_conection.recv(1024)
    request = request.decode('utf-8')
    request = request.split(" ")

    print(request)

    if(request[0] == "GET"):
        file = request[1].split(" ")
        print("FILE: " + file[0][1:])
        if(file[0] == "/"):
            index = open("index.html")
            contend = index.read()
            http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
            index.close()
        else:
            try:
                response = open(file[0][1:])
                contend = response.read()
                http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
                response.close()
            except:
                not_found = open("not_found.html")
                contend = not_found.read()
                http_response = """HTTP/1.1 404 Not Found\r\n\r\n""" + \
                    str(contend)
                not_found.close()
    else:
        bad_request = open("bad_request.html")
        contend = bad_request.read()
        http_response = """HTTP/1.1 400 Bad Request\r\n\r\n""" + str(contend)
        bad_request.close()

# Resposta do servidor
# Servidor retorna a resposta para o cliente
    client_conection.send(http_response.encode("utf-8"))
# Encerra a conexão
    client_conection.close()
# Encerra o socket do servidor
socket.close()
