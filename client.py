import socket
import threading
import time

key = 1834
isExit = False
join = False


def receivingmsg(name, sock):
	while not exit:
		try:
			while True:
				data, addr = sock.recvMsgFrom(1024)

				# Decription
				decrypt = ""
				k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i) ^ key)
				print(decrypt)
				# End of message decription

				time.sleep(0.2)
		except:
			pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.1", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host.bind((host, port))
s.setblocking(False)

alias = input("User Name: ")
rt = threading.Thread(target=receivingmsg, args=("RecvThread", s))
rt.start()

while isExit == False:
	if join == False:
		s.sendto(("[" + alias + "] --> is in chat ").encode("utf-8"), server)
		join = True
	else:
		try:
			message = input()

			# Begin
			crypt = ""
			for i in message:
				crypt += chr(ord(i) ^ key)
			message = crypt
			# End

			if message != "":
				s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

			time.sleep(0.2)
		except:
			s.sendto(("[" + alias + "] <-- gone from chat ").encode("utf-8"), server)
			shutdown = True

rt.join()
s.close()
