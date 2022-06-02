import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8080))
print("Opa servidor! conectei\n")

name_file = str(input("Nome do arquivo: ")).encode()

client.send(name_file)

open(name_file, "wb")
