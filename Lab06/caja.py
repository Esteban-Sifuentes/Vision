import Image
import sys
from math import sqrt
from time import *
import random

SobelX = ([-1,0,1],[-2,0,2],[-1,0,1])
SobelY = ([1,2,1],[0,0,0],[-1,-2,-1])

def grises(im,w,h):
    pixeles = im.load()

    gris = Image.new('RGB',(w,h))
    pix = gris.load()

    for i in range(w):
        for j in range(h):
            prom = sum(pixeles[i,j])/3
            pix[i,j] = (prom,prom,prom)
    return gris


def convolucion(im,w,h,maskX,maskY):
    pixeles =im.load()
    pix = []

    for i in range(w):
        for j in range(h):
            gx,gy = 0,0
            for x in range(3):
                for y in range(3):
                    try:
                        gx += pixeles[x+i,y+j][0]*maskX[x][y]
                        gy += pixeles[x+i,y+j][0]*maskY[x][y]
                    except:
                        pass
            G = int(sqrt(pow(gx,2)+pow(gy,2)))
            pixeles[i,j] = (G,G,G)
            pix.append(pixeles[i,j])
    return im

def binarizacion(im,w,h):
    umbral = int(raw_input('valor para binarizar:'))
    pixeles = im.load()

    binaria = Image.new('RGB',(w,h))
    pix = binaria.load()

    for i in range(w):
        for j in range(h):
            promedio =  sum(pixeles[i,j])/3
            if promedio > umbral:
                pix[i,j] = (255,255,255)
            else:
                pix[i,j] = (0,0,0)
    return binaria
####################################################################################################################
def accion(imSerializable):
    x,y = imSerializable.size
    px = imSerializable.load()
    for j in range(y):
        for i in range(x):
            pixel = px[i,j]
            if pixel == (0,0,0):
                #colornuevo = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
                colornuevo = (140,0,140)
                imSerializable = buscaForma(imSerializable, (i,j),colornuevo)

    imSerializable.show()
    return imSerializable

def buscaForma(im,referencia,color):
    forma = []
    totf = []
    px = im.load()
    alto, ancho = im.size
    forma.append(referencia)
    original = px[referencia]
    while len(forma) > 0:
        (x, y) = forma.pop(0)
        actual = px[x, y]
        if actual == original or actual == color:
            for dx in range(-1,2):
                for dy in range(-1,2):
                    pix = x+dx
                    piy = y+dy
                    if pix >= 0 and pix < alto and piy >= 0 and piy < ancho:
                        n = px[pix, piy]
                        if n == original:
                            forma.append((pix, piy))
                            totf.append((pix,piy))
                            im.putpixel((pix, piy), color)
        return im
################################################################################################################


def main():
    im = Image.open('elipse.jpg')
    w,h = im.size

    gris = grises(im,w,h)
    binaria = binarizacion(gris,w,h)
    conva = convolucion(binaria,w,h,SobelX,SobelY)

    accion(conva)

    sys.exit()
    #La imagen en convolucion se pasa al resto de los metodos                                                                                                                            
main()
