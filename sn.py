cat /usr/bin/sn
#!/usr/bin/python
import pexpect
import sys
import argparse
import ipaddress

user = sys.argv[1]
host = sys.argv[2]

print ("##########################################################")
print ("#               login to  remote server:                 #")
print ("##########################################################")
print ("#                                                        #")
print ("# base-streamer 10.100.128.20   streamer-ng 18.25.193.15 #")
print ("#     dns1home 11.200.128.9   dns2home 17.240.128.23     #")
print ("#          nx0 12.210.33.9   zaldl 16.230.0.136          #")
print ("#            crm 14.0.241.29  m9 15.9.240.99             #")
print ("##########################################################")
print ("#                                                        #")
print ("#     usage sn <user>  <device>  sn dev streamer-ng      #")
print ("#                                                        #")
print ("##########################################################")

def conn(host):
 conn = pexpect.spawn ('ssh ' + user + '@' + host)
 conn.delaybeforesend = 0
 conn.expect('assword:')
 conn.sendline(pw)
 conn.setwinsize(200,200)
 conn.interact()

try:
    if host == 'base-streamer':
        host = '10.10.10.10'
        pw = 'pass1'
        conn(host)
    if host == 'crm':
        host = '20.20.20.20'
        pw = "pass'2"
        conn(host)
    if host == 'm9':
        host = '30.30.30.30'
        pw = "pass'3"
        conn(host)
    elif host == 'streamer-ng':
        host = '40.40.40.40'
        pw = 'pass4'
        conn(host)
    elif host == 'zaldl':
        host = '50.50.50.50'
        pw = "pass5"
        conn(host)
    else: 
        conn(host)
except pexpect.EOF:
    try:
        if ipaddress.ip_address(26):
            print("password error for host")
    except ValueError:
        print('invalid host')
except pexpect.TIMEOUT:
    print('host unreachable')
