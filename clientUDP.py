from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
file = open('test.txt', mode='rb')
message = (file.read())
clientSocket.sendto(message,(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()