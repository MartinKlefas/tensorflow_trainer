# Tensorflow Trainer
Quick project to train a TensorFlow Litemodel on a directory of classified images. Based on the official tensorflow notebook https://www.tensorflow.org/lite/models/modify/model_maker/image_classification

Can't get tf model maker lite to install on my dev box, so instead I've used [this docker image and guidelines](https://github.com/waikato-datamining/tensorflow/tree/master/tflite_model_maker/docker/2.4.3) 

the script **'main.py'** will run on the docker to train a model from folders of images named after their classes. It should use your GPU if you have one, and your CPU if not. Should!

I've also included script 'image_capture.py' that will open up your default webcam and record images for each class - saving them in the appropriate format and location for you to later use in the trainer code.

For whatever reason I can't get the docker to read it's local file storage unless it's just downloaded the files itself. I therefor have used the same tgz zip/upload/download/extract workflow that's in the example code, and that seems to work fine - even if it does add a few minutes to each run.

> Written with [StackEdit](https://stackedit.io/).
