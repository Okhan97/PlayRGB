import png
import math
from random import randint

def random_img(height, width, mode):
    return [random_vector(width, mode) for _ in range(height)]

def random_vector(width, mode):
    rep = width
    if mode == "LA":
        rep *= 2
    elif mode == "RGB":
        rep *= 3
    elif mode == "RGBA":
        rep *= 4
    return [randint(0,255) for _ in range(rep)]

#500x500
def gradient_img(height, width, R=False, G=False, B=False):
    def aux1(val):
        if R and val%3 == 0:
            return math.floor(val/width/3*255)
        if G and val%3 == 1:
            return math.floor(val/width/3*255)
        if B and val%3 == 2:
            return math.floor(val/width/3*255)
        return 0
    def aux2():
        return [aux1(i) for i in range(width*3)]
    return [ aux2() for _ in range(height)]


png.from_array(gradient_img(500,500,R=True, B=True),"RGB").save("random.png")