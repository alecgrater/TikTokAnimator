from tkinter import *
from ball import *
from sound import *
import time

# create tkinter window
window = Tk()

# global variables
WIDTH = 500
HEIGHT = 500

# create the canvas
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


ball_1 = Ball(canvas, 0, 0, 100, 1, 1, "white")
ball_2 = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
ball_3 = Ball(canvas, 0, 0, 125, 3, 5, "orange")
ball_4 = Ball(canvas, 0, 0, 75, 2, 1, "black")
sound = Sound('bin/shoot.wav')

while True:
    ball_1.move()
    ball_2.move()
    ball_3.move()
    ball_4.move()
    window.update()
    time.sleep(0.01)
    sound.play()

