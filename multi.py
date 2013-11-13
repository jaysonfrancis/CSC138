#Jayson Francis // Pao Fang
#CpE 138 - Computer Networking
#Programming Assignment #1 (Socket Programming)
#Extra Credit - Multi Threaded Web Server

#Purpose of MultiThreading
#This server will consist of 2+n threads. Every time a connection is made through the tcp protocol, a new thread is then 
#created using a separate port, opening a new connection for a browser. Therefore, one connection will
#be responsible for listening to incoming HTTP request and inserting them in the queue. Another thread will
#be responsible for choosing a request from the queue and scheduling it into a thread. By doing this,
#our operating system process can manage its use by more than one user at a time, without having to run
#multiple copies of the program on the computer. This speeds up processing time and saves a lot of memory.  


#importing socket/threading module
from threading import Thread
import socket
  
class clientThread(Thread):
  def __init__(self,sock):
    Thread.__init__(self)
    self.socket = sock
    self.running = 1
 
    
  def run(self):
    try:
      #(2) receiving the http request from connection
      message = self.socket.recv(1024)
      #(3) parsing the request to determine specific file being used
      filename = message.split()[1]
      #(4) opening up the requested file from the server's file system
      f = open(filename[1:])
      output = f.read()
      #(5) create an HTTP response message consisting of the requested file preceded by header lines
      self.socket.send('\nHTTP/1.1 200 OK\n')
      self.socket.send('Connection: 37.13 miles')
      self.socket.send('Date: Todays date\n')
	  #(6) Send the response over the TCP connection to the requesting browser
      for i in range(0, len(output)):
        self.socket.send(output[i]) 

      self.socket.close()
        
      #(7) If the file is not found, return 404 not found.   
    except IOError:
      print("Client Disconnection")
      self.socket.send('404 Error File Not Found!\n')
      self.running = 0
      self.socket.close()
        
def main():
  #int a serversocket to use TCP connection
  serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  serverPort = 1337
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1)
  running = 1
  print("Multi Threaded Web Server (Cpe 138 / Jayson Francis)")
  print("Now Listening for Clients on Port:",serverPort)
  while running == 1:
    #(1) creating conncetion socket after being contacted by the browser
    connectionSocket,addrinfo=serverSocket.accept()
	#Create a new thread everytime a connection is accepeted, using 'clientThread' method
    t = clientThread(connectionSocket)
    print("Update: New client",addrinfo[0],":",addrinfo[1],"has connected!")
	#Start the new thread
    t.start()
        
  serverSocket.close()
 
if __name__ == "__main__":
  main()
