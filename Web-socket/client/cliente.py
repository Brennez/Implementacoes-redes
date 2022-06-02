from cgi import print_arguments
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8080))
print("Opa servidor! conectei\n")

name_file = str(input("Nome do arquivo: "))

client.send(name_file.encode())

with open(name_file, "wb") as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print("Arquivo recebido")
