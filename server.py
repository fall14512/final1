import socket
import threading

def accept_client():
    while True:
        #accept    
        client_sock, client_add = server_sock.accept()
        username = client_sock.recv(1024)
        CONNECTION.append((username, client_sock))
        print('%s ......connected' %username)

def transfer():
    while True:
        for i in range(len(CONNECTION)):
            try:
                data = CONNECTION[i][1].recv(1024)
                if data:
                    b_usr(CONNECTION[i][1], CONNECTION[i][0], data)
            except Exception as x:
                print(x.message)
                break

def b_usr(cs_sock, sender_name, msg):
    for i in range(len(CONNECTION)):
        if (CONNECTION[i][1] != cs_sock):
            CONNECTION[i][1].send(sender_name)
            CONNECTION[i][1].send(msg)

if __name__ == "__main__":    
    CONNECTION = []

    # socket creation
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # socket binding
    HOST = 'localhost'
    PORT = 5699
    server_sock.bind((HOST, PORT))
    # listening
    server_sock.listen(2)
    print('Chat server started on port : ' + str(PORT))

    thread_a = threading.Thread(target = accept_client)
    thread_a.start()

    thread_b = threading.Thread(target = transfer)
    thread_b.start()
