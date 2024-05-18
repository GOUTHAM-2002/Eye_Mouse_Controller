<!DOCTYPE html>
<html>
<head>
 
</head>
<body>

<h1>Eye Mouse Controller</h1>
<hr>

<p>
    This project demonstrates a simple implementation of controlling the mouse cursor using eye movement, utilizing OpenCV and MediaPipe. This is a great way to explore computer vision and human-computer interaction techniques.
</p>

<h2>Getting Started</h2>

<p>To get started with this project, follow these steps:</p>

<h3>Prerequisites</h3>
<p>Ensure you have Python installed on your system. Then, install the required libraries:</p>
<pre><code>pip install opencv-python
pip install mediapipe
pip install pyautogui
</code></pre>

<h3>Installation</h3>
<ol>
    <li>
        <p><strong>Clone the repository:</strong></p>
        <pre><code>git clone https://github.com/yourusername/eye-mouse-controller.git
cd eye-mouse-controller
</code></pre>
    </li>
    <li>
        <p><strong>Install the dependencies:</strong></p>
        <pre><code>pip install -r requirements.txt
</code></pre>
    </li>
</ol>

<h3>Running the Project</h3>
<p>To run the project, simply execute:</p>
<pre><code>python eye_mouse_controller.py
</code></pre>

<h2>Usage</h2>
<ul>
    <li>Ensure your face is well-lit and clearly visible to the webcam.</li>
    <li>Look at different parts of the screen to move the cursor.</li>
    <li>Use this functionality to integrate into any use case that requires hands-free mouse control.</li>
</ul>


<h2>How It Works</h2>
<ol>
    <li><strong>Face Detection:</strong> Utilizes MediaPipe to detect facial landmarks.</li>
    <li><strong>Eye Tracking:</strong> Identifies and tracks the position of the eyes.</li>
    <li><strong>Cursor Movement:</strong> Maps the eye movement to cursor movement using PyAutoGUI.</li>
</ol>

