# UDP_Client-Server_Decryption_Using-lfsr4bit

<br>
<p> This is the simple implementation of UPD client-server message encryption in <b> Python 3 </b>, i'm using the Linear Feedback Shift Register (LFSR) 4 bit method as the modern cryptography method </p>
<p> if u guys using python 2 you should remove all the encode() and decode() function that are called in the server and client code </p>
<p> there are 2 files in the project: </p>
<ul> 
  <li> lfsr-client</li>
  <li> lfsr-server</li>
</ul>

<h4> The Ideas </h4>
<h5> Client </h5>
<ul> 
  <li> The client enters ciphertext</li>
  <li> The client enters a U-value (4-bit)</li>
  <li> The program sends a message to the server</li>
  <li> The server will process the decryption of the ciphertext sent by the client</li>
  <li> The client will receive plaintext from the server</li>
</ul><hr>
<h5> Server </h5>
<ul> 
  <li> Message received by server (ciphertext and U)</li>
  <li> Turn messages into binary lists</li>
  <li> Turns U into an integer array and saved to temp_keystream (later used for register operations)</li>
  <li> Make a keystream with 4-bit LFSR</li>
  <li> Perform the decryption process with the formula: binMessage_int [i] XOR kestream [i] to produce a binary plaintext list</li>
  <li> Change the palintext list to a plaintext string</li>
  <li> 
Message received by server (ciphertext and U)
Turn messages into binary lists
Turns U into an integer array and saved to temp_keystream (later used for register operations)
Make a keystream with 4-bit LFSR
Perform the decryption process with the formula: binMessage_int [i] XOR kestream [i] to produce a binary plaintext list
Change the palintext list to a plaintext string
Change the plaintext string containing binary codes into characters according to the ASCII table</li>
  <li> Send results back to the client</li>
</ul>
<p> some function that used in the lfsr-server.py that i made : <p>
<ol>
  <li> 
Array_int (array), will parse the results of all array values ​​to be an integer and entered into array_int
</li> 
  <li> Array_str (array), will parse all array values ​​into strings and enter into array_str
</li> 
  <li> listToString (array), will concatenate all values ​​in the array of strings into a string stored in str1
</li>
  <li> binaryToDecimal (binary), will change the binary code entered to get the decimal value according to the ASCII table
</li>
</ol><hr>

<p> to run the program : </p>
<ol>
  <li> Dont forget to install socket.py </li> 
  <li> run the lfsr-server first</li> 
  <li> after that run the client</li>
</ol>

<p> Enjoy guys if you want to watch the complete explanation (in indonesian) <a href = "https://youtu.be/GvRabtljL_0" > Click Here </a> </p>
