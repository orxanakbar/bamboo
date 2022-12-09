import subprocess
from optparse import OptionParser 
import time
import socket

def input_option():
    inoption = OptionParser()
    inoption.add_option("-a","--address",dest="ip",help="input ip address")
    inoption.add_option("-p","--port",dest="port",help="input port")
    values=inoption.parse_args()[0]
    return values

def ip_blocked():
    values = input_option()
    if values.ip and values.port:
        subprocess.run(["sudo","iptables","-A","INPUT","-s",values.ip,"-p","tcp","--destination-port",values.port,"-j","DROP"])
    elif values.ip and not values.port:
        subprocess.run(["sudo","iptables","-A","INPUT","-s",values.ip,"-j","DROP"])
        print("If you want, you can specify the port")
    else :
        print("enter the value")

def ip_unblocked():
    values = input_option()
    if values.ip and values.port:
        subprocess.run(["sudo","iptables","-D","INPUT","-s",values.ip,"-p","tcp","--destination-port",values.port,"-j","DROP"])
    elif values.ip and not values.port:
        subprocess.run(["sudo","iptables","-D","INPUT","-s",values.ip,"-j","DROP"])
        print("If you want, you can specify the port")
    else :
        print("enter the value")

def send_packet():
    values = input_option()
    stringtosend = input("Enter the desired information :")
    port = int(values.port)
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.connect((values.ip,port))
    bytes = stringtosend.encode(encoding="latin1")
    connection.send(bytes)
    connection.close()

input_option()
print("Welcome to Bamboo")
print("1-Select this if you want to send a package")
print("2-Select this if you are trying to block a ip")
print("3-Select this if you are trying to unblock a ip")
a = input("Please choose :")
time.sleep(2)
if a == "1":
    send_packet()
elif a == "2":
    ip_blocked()
elif a == "3":
    ip_unblocked()
else:
    print("Please select the given values")
