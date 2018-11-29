import socket
import time
import urllib.request

host = socket.gethostbyname(socket.gethostname())
# host = 93.92.207.221
port = 9090
ip = urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')
# ip.decode('utf-16')
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', port))

quit = False
print("[ Server Started ]")
print(host)
print(ip)
while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode("utf-16"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        quit = True

s.close()
