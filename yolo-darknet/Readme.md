This short "hack" updates Yolo-darknet for benchmarking multiple images. In order to do this, you need to:

- Download and install with CUDA support Yolo from https://github.com/pjreddie/darknet

- Replace examples/detector.c with the one here

- Make sure you have a folder full of images (such as the one in resources folder), and replace "/root/darknet/images/" with the absolute path to that image folder

- Run Yolo as follows:

./darknet detect cfg/yolo.cfg yolo.weights 

The above works for tiny yolo also!
