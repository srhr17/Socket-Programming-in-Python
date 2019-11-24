import socket

port=60000
s=socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(5)

print('Server listening . . .')

while(True):
    conn,adr=s.accept()
    print('Got connection from ',adr)
    data=conn.recv(1024)
    print('Server Received ',repr(data))
    f=open('tec.txt','rb')
    r=f.read(1024)
    while(r):
        conn.send(r)
        print('Sent ',repr(r))
        r=f.read(1024)
    f.close()
    print('Done Sending')
    conn.send(' Thank you '.encode())
    conn.close()
