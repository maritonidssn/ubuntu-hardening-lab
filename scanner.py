import socket

for port in range(1, 1025):
	s = socket.socket()
	s.settimeout(0.1)

	if s.connect_ex(("127.0.0.1",port)) == 0: print(f"Port {port} is open")

s.close()
