# connect4-nn
Neural Network based Connect4 application in Python

This project is meant as a small experiment for me to get some practical experience in writing Python and working with
neural networks (outside of the usual Jupyter notebooks I encountered on Coursera and Kaggle).
I know that Connect4 can be solved without neural networks, but I just wanted to give it a try.

My background is Java development.  I tried to stick to the Python code-style, but I'm sure I erred here and there.

You are free to use/modify/distribute this code as you see fit.

The code was written on macOS Catalina using PyCharm and virtualenv, using Python 3.7.3(*), and the following packages
 - pygame 1.9.6
 - Tensorflow 2.0.0
 - pytest 5.3.2

This is a work in progress, but all comments/tips are welcome.
You can mail me at firstname dot lastname at telenet dot be.

Thomas Poppe

(*) I had to manually download that version of Python.  My brew installed version 3.7.5 did not work with PyGame (the
    screen was always black), and version 3.8.0 gave issues when I tried to pip install tensorflow.
