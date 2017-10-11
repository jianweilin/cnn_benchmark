#!/usr/bin/env python

import random
import socket, select
import time
from random import randint
import os
from struct import pack

#image = "output-000861.png"

print 'Reading files ...'
imageFiles = filter(lambda x: x.endswith('.png'), os.listdir('images'))
print 'Read %s files' % len(imageFiles)

HOST = '10.68.229.7' # Public IP of remote host
PORT = 5555 # Port of remote host

for image in imageFiles:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.connect(server_address)
    image_data = None
    print ('\tSending image %s' % os.path.join(os.getcwd(), 'images', image))
    with open(os.path.join(os.getcwd(), 'images', image), 'r') as fp:
    	image_data = fp.read();
	length = pack('>Q', len(image_data))
	sock.sendall(length)
	sock.sendall(image_data)
	ack = sock.recv(1)	
	sock.close()
	time.sleep(5)