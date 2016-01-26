#! /usr/bin/env python

import telnetlib
import time
from getpass import getpass 


def telnet_cisco_device(username, password, remote_conn):
    remote_conn.read_until("sername: ")
    remote_conn.write(username + '\n')
    remote_conn.read_until("assword: ")
    remote_conn.write(password + '\n' )
    time.sleep(1)
    return remote_conn.read_very_eager()
    

def telnet_cursor_connect(ip, port=23, ttimeout=3):
    remote_conn = telnetlib.Telnet(ip, port, ttimeout)
    return remote_conn

def send_command(cmd, remote_conn) :
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager() 

def main():
    USERN = raw_input("Enter Username:")
    PASSW = getpass("Enter Password:")
    CONN = telnet_cursor_connect('50.76.53.27')
    telnet_cisco_device(USERN, PASSW, CONN)
    print CONN.read_very_eager()  
    print send_command ("terminal length 0", CONN)
    print send_command ("show ip int br", CONN)
    print CONN.read_very_eager()
    print send_command ("terminal length 0", CONN)
    print send_command ("show version", CONN)

if __name__ == "__main__" :
    main()
