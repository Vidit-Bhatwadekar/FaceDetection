
# FaceDetection

I Used Pre-trained OpenCV CascadeClassifier to detect Faces, Eyes etc. Can detect via webcam or through jpgs.


![4a95q0](https://user-images.githubusercontent.com/61810502/89146460-62508700-d586-11ea-8acf-f26d9dfd9040.gif)


Dependencies:
* [OpenCV](https://opencv.org/)

You can install OpenCV using pip:
```bash
pip install opencv-python
```

### Webcam Detection

To run Webcam detector:
* Navigate to inside the repo
* Run WebcamFaceDetection.py by:

```bash
python WebcamFaceDetection.py
```
* Type either 'Face', 'Eyes', 'Left Eye' or 'Right Eye' when prompted for a 'Detection'

### Photo file Detection

To run Webcam detector:
* Navigate to inside the repo
* Place JPG file of face inside repo - not inside any folders
* Run Photo Face Detector by:

```bash
python PhotoFaceDetection.py
```

### Potential Next Steps

- To Deploy this as a webApp
- Bundle all dependencies etc. using Docker container

