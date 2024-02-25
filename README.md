# Live-Face-Blur

This project utilizes OpenCV to detect faces in real-time video streams from your webcam and blur them out. It employs a pre-trained Haar Cascade model for face detection and Gaussian blur for obscuring the detected faces.

## Installation
Ensure you have Python installed on your system along with the OpenCV library.

## Running
Your webcam will activate, and faces in the video feed will be detected and blurred out in real-time.

## Code Explanation
The script face_detection.py performs the following steps:

-Initializes the webcam capture.
-Loads the pre-trained Haar Cascade model for face detection. <br>
-Reads each frame from the webcam feed and converts it to grayscale. <br>
-Detects faces in the grayscale frame using the Haar Cascade classifier. <br>
-Draws rectangles around the detected faces. <br>
-Blurs the face regions using Gaussian blur. <br>
-Updates the frame with the blurred face regions. <br>
-Displays the modified frame with blurred faces in real-time.
