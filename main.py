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

#img to matrix
def img_to_matrix(img):
    matrix = []
    vert_cont =-1
    for line in img:
        vert_cont +=1
        line_aux = []
        horz_cont =-1
        for i in range(int(len(line)/3)):
            horz_cont +=1
            line_aux.append({
                "R": line[i*3],
                "G": line[i*3 +1],
                "B": line[i*3 +2],
                "y": vert_cont,
                "x": horz_cont
                })
        matrix.append(line_aux)
    return matrix

#matrix to img
#avoids out of boundary values
def matrix_to_img(matrix):
    img = []
    for line in matrix:
        line_aux = []
        for pix in line:
            line_aux.append(min(max(pix["R"],0),255))
            line_aux.append(min(max(pix["G"],0),255))
            line_aux.append(min(max(pix["B"],0),255))
        img.append(line_aux)
    return img

def xy_img(matrix):
    new_img = []
    for line in matrix:
        new_line = []
        for pix in line:
            new_line.append({
                "R": pix["y"]-pix["x"],
                "G": pix["y"],
                "B": pix["x"],
            })
        new_img.append(new_line)
    return new_img


img = gradient_img(500,500)
matrix = img_to_matrix(img)
new_mat = xy_img(matrix)
img2 = matrix_to_img(new_mat)
png.from_array(img2,"RGB").save("random.png")