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

def scale(name,name2,prop=2):
    img = Image.open(name)
    w,h = img.size
    pixeles = img.load()

    resized = Image.new('RGB',(w*2,h*2))
    pix2 = resized.load()
    nw,nh = resized.size


    for j in range(nh):
        for i in range(0,nw,2):
            pix2[i,j] = pixeles[i%w,j%h]
            pix2[i+1,j] = pixeles[i%w,j%h]


    resized.save(name2)
    mostrarImagen(name2)

def nomain():
    name = "jenni.png"
    name2 = "prueba.jpg"
    
    print "Como desea ver la imagen?"
    o = raw_input("NORMAL/GRISES/INVERTIDA \n")

    if o == "NORMAL":
        mostrarImagen(name)
    elif o == "GRISES":
        grises(name,name2)
    elif o == "INVERTIDA":
        invertir(name,name2)
    else:
        print "Opcion invalida"
        return
    
def main():
    name = "jenni.png"
    name2 = "prueba.jpg"
    scale(name,name2)

if __name__ == "__main__":
    main()
