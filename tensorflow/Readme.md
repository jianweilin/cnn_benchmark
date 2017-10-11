Configuration for tensorflow to do object detection benchmarking

- First install tensorflow: pip install tensorflow-gpu=1.1.0
- Second, install tensorflow models, follow guide at https://github.com/tensorflow/models
- Third, add the files in tensorflow config models to tensorflow
- Fourth replace the PATH_TO_TEST_IMAGES_DIR in object_detection_tutorial.py with the path to the images (e.g. the ones contained in the resources folder)

To run the benchmark, execute run_benchmark.sh, from the tensorflow/models/research folder
