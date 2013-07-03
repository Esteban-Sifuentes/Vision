import Image
from numpy import array,zeros
import sys
from math import floor

RobertsX = [[0,1],[-1,0]]
RobertsY = [[1,0],[0,-1]]
SobelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
SobelY = [[1,2,1],[0,0,0],[-1,-2,-1]]
PrewittX = [[-1,0,1],[-1,0,1],[-1,0,1]]
PrewittY = [[1,1,1],[0,0,0],[-1,-1,-1]]

def grises(im,w,h,pixeles):
    gris = Image.new("RGB",(w,h))
    pixs = gris.load()

    for j in range(h):
        for i in range(w):
            p = sum(pixeles[i,j])/3
            pixs[i,j] = (p,p,p)
    return gris

def normalizar(im,w,h):
    pixeles = im.load()

    normal = Image.new("RGB",(w,h))
    pixs = normal.load()

    lista = []
    for j in range(h):
        for i in range(w):
            lista.append(pixeles[i,j][0])

    maximo = max(lista)
    minimo = min(lista)

    for j in range(h):
        for i in range(w):
            pix = pixeles[i,j][0]
            new_pix = int(floor((pix-minimo)*(255.0/(maximo-minimo))))
            pixs[i,j] = (new_pix,new_pix,new_pix)
        
    normal.show()


def main():
    im = Image.open('jenni.jpg')
    w,h = im.size
    pixeles = im.load()
    im.show()

    nueva = grises(im,w,h,pixeles)
    nueva = pass

    nueva.show()


if __name__ == "__main__":
    main()
