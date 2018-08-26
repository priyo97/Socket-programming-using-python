import socket

def main():

	'''
	Half duplex communication that should initiate from the client side
	'''

    host = "127.0.0.1"
    port = 8000

    with socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM) as s:

	    s.bind((host,port))

	    s.listen(1)

	    c,addr = s.accept()

	    with c:

	    	print("Connection Established:"+str(addr))

	    	while True:

	    	    data = c.recv(1024)
	    	    
	    	    if not data:
	    	        break

	    	    data = data.decode(encoding="utf-8")
	    	    print("From Connected User:" + data)
	    	    data = data.upper()

	    	    print("Sending:" + data)
	    	    c.send(data.encode(encoding="utf-8"))
    

if __name__=="__main__":
    main()
        
