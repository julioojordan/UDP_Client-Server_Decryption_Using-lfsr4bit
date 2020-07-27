#UDP Python with stream chiper decryption LFSR
#by Julio Andyan Jordan Aryanto
#nim 24060117130078
#server

from socket import *

#mengubah array menjadi integer
def array_int(array):
    array_int = []
    for i in range(len(array)):
        array_int.append(int(array[i]))
    return array_int

#mengubah array menjadi string
def array_str(array):
    array_str = []
    for i in range(len(array)):
        array_str.append(str(array[i]))
    return array_str


#list to string
def listToString(array):
    str1 = ''
    for i in range(len(array)):
        str1 += array[i]
    return str1

#mengubah biner ke decimal
def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)



serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
print ('==============PROCESS==============')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    U, clientAddress = serverSocket.recvfrom(2048)

    #mengubah message menjadi str biner
    binMessage = ''.join(format(ord(i), 'b') for i in message.decode())

    #mengubah binMassage menjadi array integer
    binMessage_int = array_int(binMessage)

    #mengubah U menjadi array integer
    temp_keystream = U.decode()
    temp_keystream = array_int(temp_keystream)
    
    #mengambil panjang pesan
    panjang_pesan = len(binMessage)

    #membuat keystream ide : LFSR 4 bit
    keystream = [] #inisialisasi keystream
    for i in range(panjang_pesan):
        add = temp_keystream[3] ^ temp_keystream[0]
        temp_keystream[3] = temp_keystream[2]
        temp_keystream[2] = temp_keystream[1]
        temp_keystream[1] = temp_keystream[0]
        temp_keystream[0] = add
        register = array_str(temp_keystream)
        print ("isi register "+str(i)+" = "+" ".join(register))
        keystream.append(add)
    keystream_str = array_str(keystream)

    #melakukan proses dekripsi binMessage_int[i] XOR kestream [i]
    plain = []
    for i in range(panjang_pesan):
        c = binMessage_int[i] ^ keystream[i]
        plain.append(c)
    plain_str = array_str(plain)
    
    #mengubah list plain int menjadi list str
    lstr_plain = array_str(plain)
    #list cipher str diubah ke dalam string dulu menggunakan
    #fungsi listTostring
    str_plain = listToString(lstr_plain)

    #mengubah ke dalam ASCII dan menyimpan ke cipherteks
    plainteks = ''
    for i in range(0, len(str_plain), 7): 
      
        # memotong array cipher ke index range [0, 6] 
        # dan menyimpannya ke temp_data 
        temp_data = int(str_plain[i:i + 7]) 
       
        # memasukan temp_data kefungsi binarytoDecimal 
        decimal_data = BinaryToDecimal(temp_data) 
       
        # Deccoding nilai decimal hasil dari  
        # BinarytoDecimal() function, menggunakan chr()  
        # function yang akan menghasilkan string yang sesuai  
        # dengan karakter di tabel ASCII dan menyimpan ke
        # str_data 
        plainteks = plainteks + chr(decimal_data)

    print ('==============Result==============')
    print("Pesan Diterima : "+message.decode())
    print("Biner          : "+" ".join(binMessage))
    print("Keystream      : "+" ".join(keystream_str))
    print("Plain biner    : "+" ".join(plain_str))
    print("Plainteks      : "+ plainteks)

    message = "Plainteks yang didapat dari dekripsi stream cipher dengan U ="+U.decode()+" adalah :" +plainteks
    message = bytes(message, 'utf-8')
  
    serverSocket.sendto(message, clientAddress)
