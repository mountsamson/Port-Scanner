import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = s.settimeout(5)

host = input("Enter ip address to scan ports: ") 
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    elif timeout >= 5:
        print("ERROR - timeout due to long time connnection")
    else:
        print("The port is open")

portScanner(port)




