# Jayson Francis
# CSC 138 - Computer Networking
# Programming Assignment 2 - SMTP Client
# Last Modified 11/17/2013

# Importing modules, included ssl and base64
from socket import *
import ssl
import base64

print '\n-----------------------------------\n'
print '----- Computer Networking 138 -----\n'
print '------- By: Jayson Francis --------\n'
print '-----------------------------------\n'

msg = "\r\n I love computer networks!"
endmsg ="\r\n.\r\n"

# -----------------------------------
# Choose a mail server
mailserver = 'smtp.gmail.com'
mailport = 587
 
cc = socket(AF_INET, SOCK_STREAM)
cc.connect((mailserver, mailport))

recv1 = cc.recv(1024)
print recv1
if recv1[:3] != '220':
  print '220 reply not received from server.'
# -----------------------------------


# -----------------------------------
# Send EHLO command to server.
ehloCommand = 'EHLO smtp.google.com \r\n'
cc.send(ehloCommand)

recv1 = cc.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not recieved from server.'
# -----------------------------------


# -----------------------------------	
# Starting TTL Protocol request 
cc.send('STARTTLS\r\n')

recv1 = cc.recv(1024)
print recv1
if recv1[:3] != '220':
  print '220 reply not recieved from the server' 
# -----------------------------------


# -----------------------------------
# Implementing our connection with SSL, then sending an AUTH request
SMTPClientSocket = ssl.wrap_socket(cc, ssl_version=ssl.PROTOCOL_SSLv23)
SMTPClientSocket.send('auth login\r\n')  

recv = SMTPClientSocket.recv(1024)
print recv
# -----------------------------------  



# -----------------------------------
# Here we are now sending our username and password to the server
SMTPClientSocket.send(base64.b64encode('jaysonfrancis')+'\r\n')
recv = SMTPClientSocket.recv(1024)
print recv

SMTPClientSocket.send(base64.b64encode('password')+'\r\n')
recv = SMTPClientSocket.recv(1024)
print recv
# -----------------------------------




# -----------------------------------
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
SMTPClientSocket.send(heloCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not received from server.'
# -----------------------------------



# -----------------------------------  
# Send MAIL FROM command and print server response
mailFrom = 'MAIL FROM:<jaysonfranci@gmail.com>\r\n'
print mailFrom
SMTPClientSocket.send(mailFrom)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not received from the server.'
# -----------------------------------



# -----------------------------------
# Send RCPT TO command and print server response
mailRCPT = 'RCPT TO:<jaysonfrancis@gmail.com>\r\n'
print mailRCPT
SMTPClientSocket.send(mailRCPT)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not recieved from the server.'
# -----------------------------------  
  
  
  
# -----------------------------------  
# Send DATA command and print server response
mailData = 'DATA\r\n'
print mailData
SMTPClientSocket.send(mailData)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
  print '354 reply not recieved from the server.'
# -----------------------------------  


  
# -----------------------------------
# Send Message Data  
message = raw_input("Enter Your Message: ")  
# -----------------------------------



# -----------------------------------
# Message Ends with Single Period.
mailMessageEnd='\r\n.\r\n'
SMTPClientSocket.send(message + mailMessageEnd)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not recieved from the server.'
# -----------------------------------
  
  
  
# -----------------------------------  
# Send QUIT command and get server response
quitMessage = 'QUIT\r\n'
print quitMessage
SMTPClientSocket.send(quitMessage)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
  print '221 reply not recieved from the server.'
# -----------------------------------
  
#End of File