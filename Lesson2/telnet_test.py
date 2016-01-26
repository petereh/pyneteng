#! /usr/bin/env python

import telnetlib
import time
from getpass import getpass 


def telnet_cisco_device(username, password, remote_conn):
    remote_conn.read_until("sername: ", 3)
    remote_conn.write(username + '\n')
    remote_conn.read_until("assword: ", 3)
    remote_conn.write(password )
    output = remote_conn.read_very_eager()
    return output 

def telnet_cursor_connect(ip, port=23, ttimeout=3):
    remote_conn = telnetlib.Telnet(ip, port, ttimeout)
    return remote_conn

def main():
    USERN = raw_input("Enter Username:")
    PASSW = getpass("Enter Password:")
    CONN = telnet_cursor_connect('50.76.53.27')
    CONN.read_until("sername: ")
    CONN.write(USERN + '\n')
    CONN.read_until("assword: ")
    CONN.write(PASSW + '\n')
    time.sleep(1)
    print CONN.read_very_eager()
    CONN.write("show ip int br" + '\n')
    time.sleep(1)
    print CONN.read_very_eager()  

if __name__ == "__main__" :
    main()
