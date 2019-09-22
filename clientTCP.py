from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

file = open('test.txt', mode='rb')  
sentence = (file.read())


clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence) 
clientSocket.close()
