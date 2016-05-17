# A server can be created using sockets. Sockets work on the application layer,
# it does not specify any protocol and on this level you’d define an application protocol yourself.
# Creation of a socket server needs these steps:
# bind socket to port
# start listening
# wait for client
# receive data


import socket
import sys

HOST = ''
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('# Socket created')

# Create socket on port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('# Bind failed. ')
    sys.exit()

print('# Socket bind complete')

# Start listening on socket
s.listen(10)
print('# Socket now listening')

# Wait for client
conn, add = s.accept()
print('# Connected to ' + add[0] + ':' + str(add[1]))

# Receive data from client
while True:
    data = conn.recv(1024)
    line = data.decode('UTF-8')  # convert to string (Python 3 only)
    line = line.replace("\n", "")  # remove newline character
    print(line)

s.close()


# Once running it will wait for messages.
# To connect with it, use telnet or modify the socket client from the previous section.
