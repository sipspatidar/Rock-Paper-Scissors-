import socket
import threading
import random
class game(threading.Thread):
	dict = {1:'r',2:'p',3:'s'}
	valid_input = ['r','s','p','S','R','P']
	error = "invalid input pls try again"
	def __init__(self,name,c,addr):
		threading.Thread.__init__(self)
		self.name = name
		self.c = c
		self.addr = addr
		
	def run(self):
		self.user_name = self.c.recv(1024).decode("utf-8")
		print("Game started of user "+self.user_name)
		gameover = 1
		while gameover:
			user_input = self.c.recv(1024).decode("utf-8")
			if user_input in game.valid_input:
				c = random.choice([1,2,3])
				comp = game.dict[c]
				if user_input == 'r' and comp == 's' or user_input == 's' and comp == 'p' or user_input == 'p' and comp == 'r':
					result = "you win"
				elif user_input == comp:
					result = "Draw"
				else:
					result = "you lose"
				print("sending to user "+self.user_name+" "+result)
				self.c.send(result.encode("utf-8"))
			else:
				self.c.send("invalid input pls try again".encode("utf-8"))
def Main():
	host = "127.0.0.1"
	port = 5000
	
	s = socket.socket()
	s.bind((host,port))
	
	s.listen(3)
	for i in range(3):
		print(str(i))
		c,addr = s.accept()
		print("connect with "+str(i))
		print("starting Game..... with "+str(i))
		game(str(i),c,addr).start()

if __name__ == "__main__":
	Main()