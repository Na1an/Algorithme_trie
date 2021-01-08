#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTK
from time import time, sleep
from random import choice, uniform, randint
from math import sin, cos, radians

root = tk.Tk()
w = tk.Label(root, text="Hello Tkinter")
w.pack()
root.mainloop()

class part:
    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx=0., vy=0., size=2., color='red', lifespan=2, **kwargs ):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
