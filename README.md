# Stop Sign Detection
  This project is improved for identifying stop sign in an image. To analyze image, HSV color spaces are used. Also, there is some restrictions for preventing noise and increasing consistency. The detection includes two main constraints to reduce noise and improve accuracy: number of edges and object size. 

# Necessary Libraries
  OpenCV is a library that is used for image processing. It helps to recognize objects with respect to their features. There is wide range of methods, approaches and functions. Also, it has huge documentation and open sources. These make OpenCV useful for image processing.
  To install OpenCV: pip install opencv-python
  
  Numpy is a library used for matrix operations and numerical computations. It is especially useful in image processing for handling image arrays and performing mathematical transformations efficiently.
  To install Numpy: pip install numpy
  
  Pathlib is a built-in library that is used to make path operations easy. Via path function, path's various features are easily used.

# Limitations
  Owing to the fact that the method relies on color analysis, there can be irrelevant outputs. In other words, objects like vehicle lights can deceive the code. Also, low brightness and different conditions can make inefficient measurement.

  
  

