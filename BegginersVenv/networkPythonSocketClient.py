# Socket client example in python

# Sockets are the basis of any network communication in your computer.  If you open a website,
# a socket is created in the background. The same thing applies to chat applications or any other network application.
# Python simple socket client
# We will create a simple socket client, that mimics a web browser. The web uses port 80.
# The steps a web browser does to get a web page are:
#
# create socket
# get server ip address from domain name
# connect to server using ip address
# send request to server
# receive data (web page)


import socket
import sys

host = 'www.google.com'
port = 80  # web

# create socket
print('# Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip, port))

# Send data to remote server
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request.encode())
except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = s.recv(4096)

print(reply)
