# Final project
Final Project - Graduation in Computer Engineering UERJ

## Initial Test
These implementations were made according to this [video](https://www.youtube.com/watch?v=mCcPmlr7y3U&t=511s). Using the [OpenCV](https://pypi.org/project/opencv-python/) and [MediaPipe](https://google.github.io/mediapipe/) libraries.

### OpenCV
Cross-platform library that has modules for image and video processing, linear algebra, data structure, graphical user interface, etc. It has algorithms that help in camera calibration, object recognition, structural analysis and image filtering. This library was developed in C/C++, but it supports languages ​​such as Java and Python.

```
pip install opencv-python
```

### Mediapipe
Google framework used to build machine learning pipelines for processing data related to audio, video, etc. This framework was developed in C++, JAVA and Obj-C, and its structure consists of 3 main APIs:

- Calculator API
- Graph building API
- Graph execution API

MediaPipe has open source models, that is, solutions already made by others that can be used by the community. These are made on a pre-trained TensorFLow or TFLite model according to the specific case. In this case, we will use the solution that addresses face detection.

```
pip install mediapipe
```
