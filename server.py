#!/usr/bin/python
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print 'Got connection from', addr
  while True:
    recv_line = c.recv(1024)
    print recv_line
    if recv_line == 'PING\r':
      time_s = str(time.time())
      c.send('PONG ' + time_s)
    break
  c.close()
