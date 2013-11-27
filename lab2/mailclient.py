# Jayson Francis

from socket import *

import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg ="\r\n.\r\n"

# Choose a mail server
mailserver = 'smtp.gmail.com'
mailport = 465

# Create socket to establish TCP Connection
clientSocket = socket(AF_INET, SOCK_STREAM)
SMTPClientSocket = ssl.wrap_socket(clientSocket)
SMTPClientSocket.connect((mailserver, mailport))



recv = SMTPClientSocket.recv(1024)
print recv
if recv[:3] != '220':
  print '220 reply not received from server.'
  
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
SMTPClientSocket.send(heloCommand)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not received from server.'
  
# Send MAIL FROM command and print server response
mailFrom = 'MAIL FROM: <jaysonfrancis@gmail.com>\r\n'
print mailFrom
SMTPClientSocket.send(mailFrom)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not received from the server.'

# Send RCPT TO command and print server response
mailRCPT = 'RCPT TO: <jaysonfrancis@gmail.com>\r\n'
print mailRCPT
SMTPClientSocket.send(mailRCPT)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not recieved from the server.'
  
# Send DATA command and print server response
mailData = 'DATA\r\n'
print mailData
SMTPClientSocket.send(mailData)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
  print '354 reply not recieved from the server.'

# Send Message Data  
message = raw_input("Enter Your Message: ")  

# Message Ends with Single Period.
mailMessageEnd='\r\n.\r\n'
SMTPClientSocket.send(message + mailMessageEnd)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
  print '250 reply not recieved from the server.'
  
# Send QUIT command and get server response
quitMessage = 'QUIT\r\n'
print quitMessage
SMTPClientSocket.send(quitMessage)
recv1 = SMTPClientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
  print '221 reply not recieved from the server.'
  
#End of File