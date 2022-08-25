import socket 
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET CORRESPONS TO IPV4  an internet protocol and Sock STREAM  is a tcp transmition control protocol
s.connect((socket.gethostname(),1235))
while True:
    fullmsg= ""
    newmsg = True

    while True:#buffer data 
        msg = s.recv(16)#how many chunks of data would we like to receive 
        if newmsg:
            print(f'new message lenght: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            newmsg=False
        fullmsg += msg.decode("utf-8")

        if len(fullmsg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(fullmsg[HEADERSIZE:])
            newmsg = True
            fullmsg = ""


    print(fullmsg)
""""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET CORRESPONS TO IPV4  an internet protocol and Sock STREAM  is a tcp transmition control protocol
s.connect((socket.gethostname(),1234))

fullmsg= ""
while True:#buffer data 
    msg = s.recv(1024)#how many chunks of data would we like to receive 
    if len(msg) <=0:
        break
    fullmsg += msg.decode("utf-8")


    
print(fullmsg)
"""