import socket
def Main():
	host = "127.0.0.1"
	port = 5000
	
	s = socket.socket()
	s.connect((host,port))
	
	message = input("Enter your name : ")
	s.send(message.encode('utf-8'))
		
	while message!='q':
		user_input = input("Enter r-Rock , s-Scissor , p-Paper ")
		s.send(user_input.encode("utf-8"))
		data = s.recv(1024).decode('utf-8')
		print("Recieved dom Server : "+data)
		
	s.close()
if __name__=='__main__':
	Main()