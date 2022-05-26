import os
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from Socketserver import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

# Vai ler a porta que a aplicação será executada
PORTA = int(os.getenv('PORTA', 8000))
# diretório que conterá os arquivos
os.chdir('pages')

http = Server(("", PORTA), Handler)

try:
    print("SERVIDOR RODANDO NA PORTA {}".format(PORTA))
    http.serve_forever()
except KeyboardInterrupt:
    pass
http.server_close()
