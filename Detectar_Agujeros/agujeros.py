from Tkinter import *
from PIL import ImageTk, Image, ImageDraw
from numpy import zeros,where
import sys

def grises(im,w,h,pixeles,prueba,pix):
    for i in range(w):
        for j in range(h):
            p = sum(pixeles[i,j])/3
            pix[i,j] = (p,p,p)
    return prueba,w,h,pix

def isItAgujero(x,y,pixeles,im,opcion):
    mascara = [[1,1,1],[1,1,1],[1,1,1]]

    promedio = 0
    for i in range(-1,2):
        for j in range(-1,2):
            promedio += pixeles[x+i,y+i][1] * mascara[i+1][j+1]

    promedio /= 9
    print promedio

    if opcion == "o":
        #if promedio < 50:
        if promedio < 20:
            draw = ImageDraw.Draw(im)
            draw.rectangle([(x-4,y-4),(x+4,y+4)],outline="#fc1a0a")

    elif opcion == "c":
        if promedio > 168:
            draw = ImageDraw.Draw(im)
            draw.rectangle([(x-4,y-4),(x+4,y+4)],outline="#fc1a0a")


def detect(im,w,h,pixeles,opcion):
    matrix = zeros((w,h))
    
    for i in range(w):
        for j in range(h):
            matrix [i][j] = pixeles[i,j][1]
            
    columnas = matrix.sum(0) #Sumatoria de columnas
    filas = matrix.sum(1) #Sumatoria de filas

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    candidatos = []
    
    if opcion == "o":
        for i in range(1,w-1):
            for j in range(1,h-1):
                if filas[i-1] > filas[i] < filas[i+1] and columnas[j-1] > columnas[j] < columnas[j+1]:
                    candidatos.append([i,j])

    elif opcion == "c":
        for i in range(1,w-1):
            for j in range(1,h-1):
                if filas[i-1] < filas[i] > filas[i+1] and columnas[j-1] < columnas[j] > columnas[j+1]:
                    candidatos.append([i,j])

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #Do the line
    draw = ImageDraw.Draw(im)
    for elemento in candidatos:
        x = elemento[0]
        y = elemento[1]
        if matrix[x][y] < 20:
            draw.line((x,0,x,h),fill=(0,240,0))
            draw.line((0,y,w,y),fill=(0,0,200))
            isItAgujero(x,y,pixeles,im,opcion)
        else:
            pass
    del draw
    im.show()
    im.save("Agujeros_detected.png")

def main():

    opcion = raw_input("Detectar circulos claros u oscuros? [c/o]")
    if opcion == "c":
         im = Image.open('agujeros2.jpg')
    elif opcion == "o":
         im = Image.open('agujeros3.jpg')

    w,h = im.size
    pixeles = im.load()
    prueba = Image.new("RGB",(w,h))
    pix = prueba.load()

    gris,width,height,pix = grises(im,w,h,pixeles,prueba,pix)    


    detect(gris,width,height,pix,opcion)

if __name__ == "__main__":
    main()
