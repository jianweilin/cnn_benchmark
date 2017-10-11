This utility allows an "as-a-service" approach to pyFasterRCNN. It consists of a client which sends images to a server.

Server prep:

- Clone and install py-faster-rcnn from https://github.com/rbgirshick/py-faster-rcnn

- Put the "recvimage.py" file in the tools folder of py-faster-rccn installation

- Modify recvimage.py HOST and PORT to point to the local server public IP and a port it should listen to. These should be replicated on the client.

- Run recvimage.py

Client prep:

- Make sure you have python installed

- Make sure the HOST and PORT point to the server IP and port where the recvimage service listens to

- Put images in the file (you can use images from "resources" folder)
