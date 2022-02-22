import socket
"""
if __name__ == '__main__':
    print('PyCharm')
"""
serverName = '0.0.0.0'#socket.gethostname()
serverPort = 6699
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # gerekirse kullan :
# #the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
serverSocket.bind((serverName, serverPort))
serverSocket.listen(5) #5 can change (backlog)

ignoreList = ['/favicon.ico'] #bu requestler ignore edilecekler
while True:
    #baglantiyi kabul et
    (clientSocket, address) = serverSocket.accept()

    # Get the client request
    request = clientSocket.recv(1024).decode()
    print(request)

    #process request
    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/': #GET / HTTP1.1 -> index olmali
        filename = '/index.html'
    elif filename in ignoreList:
        continue
    #check requested file exists
    try:
        file = open('source' + filename)
        content = file.read()
        file.close()
        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
        print("filename :"+filename)
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    # Send HTTP response
    clientSocket.sendall(response.encode())
    clientSocket.close()


serverSocket.close()
