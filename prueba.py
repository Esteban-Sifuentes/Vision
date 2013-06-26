import Image
import pygame
from pygame.locals import *
import sys


def mostrarImagen(name):
    im = Image.open(name)
    w,h = im.size
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    imagen = pygame.image.load(name)
    
    screen.blit(imagen,(0,0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def grises(name, name2):
    img = Image.open(name)
    w,h = img.size
    pixeles = img.load()
    
    for j in range(h):
        for i in range(w):
            prom = (sum(pixeles[i,j]))/3
            pixeles[i,j] = (prom,prom,prom)

    img.save(name2)
    mostrarImagen(name2)
    
def invertir(name,name2):
    img = Image.open(name)
    w,h = img.size
    pixeles = img.load()

    for j in range(h):
        for i in range(w):
            r,g,b = pixeles[i,j]
            pixeles[i,j] = (255-r,255-g,255-b)

    img.save(name2)
    mostrarImagen(name2)

def main():
    name = "jenni.png"
    name2 = "prueba.jpg"
    
    #mostrarImagen(name)
    
    #grises(name,name2)

    invertir(name,name2)

if __name__ == "__main__":
    main()
