import socket
import random

#create socket: AF_INET refers to ipv4, and SOCK_STREAM is TCP
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0', 6000)) #local host
#serv.bind((socket.gethostname(), 6000))
serv.listen(5) #listen for upto 5 connections

while (True):
    conn, addr = serv.accept()   #create and accept connection
    from_client = ' ' 
    while (True):
        data = conn.recv(4096)   #reveive data from client
        if not data: break       #if no data break
        from_client += data      
        print from_client
        bool_value = random.randint(0,1)  #create random int
        if(bool_value == 1):          
            print "bool_value = " + str(bool_value)
            conn.send("True")        #if value = 1 send "True" to client
        else:
            print "bool_value = " + str(bool_value)
            conn.send("False")       #else send "False to client"
     
     conn.close                    #close connection and socket
     print 'client disconnected'   #print to console that client is disconnected
