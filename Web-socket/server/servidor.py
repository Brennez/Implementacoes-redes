import socket

# Enderaço IPV4 utilizando a conexão TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 8080))
server.listen(2)
print("Servidor rodando...")
connection, address = server.accept()

# informa quantos bytes o servidor vai receber
name_file = server.recv(1024).decode()
print("Opa amigo, recebi! ")

with open(connection, 'rb') as file:
    for data in file.readlines():
        connection.send(data)
    print("pagina enviada!")
