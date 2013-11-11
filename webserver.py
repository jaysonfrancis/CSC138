#Jayson Francis // Pao Fang
#CpE 138 - Computer Networking
#Programming Assignment #1 (Socket Programming)

# (1) Web server will create a connection socket when contacted by a client (browser)
# (2) Receive the HTTP request from this connection
# (3) Parse the request to determine the specific file being requested
# (4) Get the requested file from the server's file system
# (5) Create an HTTP response message consisting of the requested file preceded by header lines
# (6) Send the response over the TCP connection toe the requesting browser. 
# 	- If the file is not found, server return a "404 Not Found" error message

# (Extra Credit) Use a multi-threaded webserver and explain how it works and its performance
# Extra credit is in the multi.py file , where we change the program to use threads
# ------------------------------------


#importing socket module
from socket import *
import time

#int a serversocket to use TCP connection
serverSocket = socket(AF_INET, SOCK_STREAM)

#establishing server port to listen too
serverPort = 1337
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print 'Status: Listening on port: ', serverPort


while True:
  #(1) creating conncetion socket after being contacted by the browser
  connectionSocket, addr = serverSocket.accept()
  try:
    #(2) receiving the http request from connection
    message = connectionSocket.recv(1024)

    #(3) parsing the request to determine specific file being used
    filename = message.split()[1]

    #(4) opening up the requested file from the server's file system
    f = open(filename[1:])
    output = f.read()

    #(5) create an HTTP response message consisting of the requested file preceded by header lines
    connectionSocket.send('\nHTTP/1.1 200 OK\n')
    connectionSocket.send('Connection: 37.13 miles')
    connectionSocket.send('Date: Todays date\n')
    connectionSocket.send('Server: Server information\n')
    connectionSocket.send('Last-Modified: Now\n')
    connectionSocket.send('Content-Length: 1024\n')
    connectionSocket.send('Content-Type: text/html\n\n')

    #(6) Send the response over the TCP connection to the requesting browser
    for i in range(0, len(output)):
      connectionSocket.send(output[i])
    connectionSocket.close()
    print 'File successfully recieved.'

    #(7) If the file is not found, return 404 not found.
  except IOError:
        print 'Error: 404 Request sent to client'
        connectionSocket.send('404 Error File Not Found!\n')
        connectionSocket.close()

print 'Server now unavailable'
serverSocket.close()




#-------------------------------------
#End of file






