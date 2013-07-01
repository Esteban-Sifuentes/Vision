import Image
from numpy import array,zeros
import pygame
from pygame.locals import *
import sys

RobertsX = array([[0,1],[-1,0]])
RobertsY = array([[1,0],[0,-1]])
SobelX = array([[-1,0,1],[-2,0,2],[-1,0,1]])
SobelY = array([[1,2,1],[0,0,0],[-1,-2,-1]])
PrewittX = array([[-1,0,1],[-1,0,1],[-1,0,1]])
PrewittY = array([[1,1,1],[0,0,0],[-1,-1,-1]])

def abrirImagen(name,w,h):
    pygame.init()
    
    pantalla = pygame.display.set_mode((w,h))
    imagen = pygame.image.load(name)

    pantalla.blit(imagen,(0,0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def grises(im,pixs,w,h):
    name2 = "gris.jpg"
    for j in range(h):
        for i in range(w):
            prom = sum(pixs[i,j])/3
            pixs[i,j] = (prom,prom,prom)
    im.save(name2)
    im.show(now)
    #abrirImagen(name2,w,h)
    return name2
    

def main():
    name = "jenni.png"
    im = Image.open(name)
    w,h = im.size
    pixs = im.load()
    #abrirImagen(name,w,h)
    gris = grises(im,pixs,w,h)


    #abrirImagen(name,w,h)


if __name__ == "__main__":
    main()
