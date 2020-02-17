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

There are 3 files that are meant to be run:
- connect4.py: play a game against the computer
- learn.py: let the computer play itself and let it try to learn from it
- simulate.py: show how the computer plays itself, to get a feel for its level

Current state: after a few million games, the computer is still barely smarter than random playing.  Once it has been
learning for a bit longer, I will update this file and check in the learned model.

Mistakes I have made so far:
- giving boards a score between -1 (loosing) and 1 (winning), but sigmoid (outputting between 0 and 1) in the last layer 
  instead of tanh (outputting between -1 and 1)
- not switching the "viewpoint" of the board states of the second player (see the "factor" in the GameGenerator code
  and in the adapted board state in the NNStrategy.__predict_value method)
- Ignoring tie games - now each player scores half a point for a tie game
- Using binary_crossentropy loss (which is meant for classification, where this is a regression problem), and trying to 
  measure accuracy (which was always 0).

This is a work in progress, but all comments/tips are welcome.  Please help me enlarge the list above :)
You can mail me at firstname dot lastname at telenet dot be.

Thomas Poppe

(*) I had to manually download that version of Python.  My brew installed version 3.7.5 did not work with PyGame (the
    screen was always black), and version 3.8.0 gave issues when I tried to pip install tensorflow.
