# Import socket module
import socket
# Activate socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to a host
mysock.connect(('data.pr4e.org', 80))
# Send and encode a command to a host
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# Retrieve 512 characters until there's no more data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
# Close socket connection
mysock.close()
