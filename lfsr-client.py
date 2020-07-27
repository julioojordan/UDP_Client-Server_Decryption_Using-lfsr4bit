#UDP Python with stream chiper decryption LFSR

#by Julio Andyan Jordan Aryanto
#nim 24060117130078
#DIPONEGORO UNIVERSITY
# IT 17
#client

from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Masukan Cipherteks:') #input the cipherteks
U = input('Masukan nilai U (4 bit): ') # input U

#mengirimkan pesan ke server / send a message to the server
clientSocket.sendto(message.encode(),(serverName, serverPort))
clientSocket.sendto(U.encode(),(serverName, serverPort))


#mengambil pesan dari server / take a message from the server
message, serverAddress =clientSocket.recvfrom(2048)

#menampilkan pesan / showing the message
print (message.decode())
clientSocket.close()
