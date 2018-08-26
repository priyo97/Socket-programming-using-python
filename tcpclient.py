import socket


def main():
	'''
	Half duplex communication that should initiate from the client side
	'''
	remote_host = "127.0.0.1"
	port = 8000

	# ip = socket.gethostbyname(host)

	with socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM) as s:


		s.connect((remote_host,port))

		while True:

			msg = input("Enter a message:")
			msg = msg.encode(encoding="utf-8")
			s.send(msg)

			response = s.recv(1024)
			response = response.decode(encoding="utf-8")

			print("=>" + response)

if __name__ == '__main__':
	main()
		















    
    

