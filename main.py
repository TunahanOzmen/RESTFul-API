import socket
import GET_funcs
import Handler

serverName = '0.0.0.0'
serverPort = 5599
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

ignoreList = ['/favicon.ico'] #bu requestler ignore edilecekler - chrome tarafindan server acilirsa gonderiliyor
while True:
    # Accept client
    (clientSocket, address) = serverSocket.accept()

    # Get the client request
    request = clientSocket.recv(1024).decode()
    headers = request.split('\n')
    METHOD = headers[0].split()[0]

    if(headers[0].split()[1] in ignoreList):
        continue
    # Process the client request
    if METHOD == 'GET':
        try:
            response = Handler.handleGetRequests(headers)
            response = "HTTP/1.1 200 OK\n\n"+response
        except:
            response = "HTTP/1.1 500 Internal Server Error\n\n" + "An Error Occured"
    elif METHOD == 'POST':
        try:
            response = Handler.handlePostRequests(headers)
            response = "HTTP/1.1 200 OK\n\n" + response
        except:
            response = "HTTP/1.1 500 Internal Server Error\n\n" + "An Error Occured"

    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nUnknown Request, Try GET or POST requests'

    # Send a response to client
    print("Response Sent to ", address)
    clientSocket.sendall(response.encode())

    # Close connection
    clientSocket.close()

serverSocket.close()
