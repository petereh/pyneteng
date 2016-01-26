#! /usr/bin/env python

import telnetlib
import time
import socket
import sys
from getpass import getpass 


def telnet_cisco_device(username, password, remote_conn):
    remote_conn.read_until("sername: ")
    remote_conn.write(username + '\n')
    remote_conn.read_until("assword: ")
    remote_conn.write(password + '\n' )
    time.sleep(1)
    return remote_conn.read_very_eager()
    

def telnet_cursor_connect(ip, port=23, ttimeout=3):
    try:
        remote_conn = telnetlib.Telnet(ip, port, ttimeout)
        return remote_conn
    except (socket.error,AttributeError) :
        sys.exit( "Error!!! Please Ensure you have entered the correct IP address , username and Password")

def send_command(cmd, remote_conn) :
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager() 

def main():
    USERN = raw_input("Enter Username:")
    PASSW = getpass("Enter Password:")
    IP = raw_input("Enter IP address")
    CONN = telnet_cursor_connect(IP)
    telnet_cisco_device(USERN, PASSW, CONN)
    CONN.read_very_eager()  
    send_command ("terminal length 0", CONN)
    print send_command ("show ip int br", CONN)
    CONN.read_very_eager()
    send_command ("terminal length 0", CONN)
    print send_command ("show version", CONN)
    CONN.close ()

if __name__ == "__main__" :
    main()
