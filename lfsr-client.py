#UDP Python with stream chiper decryption LFSR

#by Julio Andyan Jordan Aryanto
#nim 24060117130078
#client

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Masukan Cipherteks:')
U = input('Masukan nilai U (4 bit): ')

#mengirimkan pesan ke server
clientSocket.sendto(message.encode(),(serverName, serverPort))
clientSocket.sendto(U.encode(),(serverName, serverPort))


#mengambil pesan dari server
message, serverAddress =clientSocket.recvfrom(2048)

#menampilkan pesan
print (message.decode())
clientSocket.close()
