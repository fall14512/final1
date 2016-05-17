import socket
import threading

def to_send():
    while True:
        msg = raw_input('\n > ')
        client_sock.send(msg)

def to_receive():
    while True:
        sender_name = client_sock.recv(1024)
        data = clint_sock.recv(1024)

        print('\n' + str(sen_name) + ' > ' + str(data))

if __name__ == "__main__":

    
    # socket created
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5699
    client_sock.connect((HOST, PORT))     
    print('Connected.......')
    username = raw_input('Enter name to enter chat... ')
    client_sock.send(username)

    thread_send = threading.Thread(target = to_send)
    thread_send.start()

    thread_receive = threading.Thread(target = to_receive)
    thread_receive.start()
