from http import client
import socket 
HEADERSIZE = 10
 
#HEADERS INFORM YOUR PROGRAM ABOT THE AMOUNT OF INFORMATION 
""""### CODE THAT SENDS DATA OVER YOUT DATA BUFFER SIZE BY CLOSING THE SERVER 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET CORRESPONS TO IPV4  an internet protocol and Sock STREAM  is a tcp transmition control protocol
s.bind((socket.gethostname(), 1234))
s.listen(5) #que of five

while True:
    clientsocket, address = s.accept() #client socket obj and ip address
    print(f"connection with {address} has been established")
    clientsocket.send("WELCOME TO THE SERVER".encode())
    clientsocket.close()
    """

#HOW TO HANDLE SOCKETS THAT EXIT YOUR BUFFER MEASURE BUT YOU DO NOT WANT TO CLOSE THE CONECTION (USING A HEADER)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET CORRESPONS TO IPV4  an internet protocol and Sock STREAM  is a tcp transmition control protocol
s.bind((socket.gethostname(), 1235))
s.listen(5) #que of five

while True:
    clientsocket, address = s.accept() #client socket obj and ip address
    print(f"connection with {address} has been established")
    msg = "WELCOME TO THE SERVER"
    msg= f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(msg.encode())
