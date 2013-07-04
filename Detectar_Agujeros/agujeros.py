from Tkinter import *
from PIL import ImageTk, Image, ImageDraw
from numpy import zeros,where
import sys

def showing():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('agujero.png'))
    texto = 'Agujero'


    w = Label(root,
              compound = (0,0),
              text = texto,
              foreground = '#FFFF00',
              image = img).pack(side='right')

    root.mainloop()

def grises(im,w,h,pixeles,prueba,pix):
    for i in range(w):
        for j in range(h):
            p = sum(pixeles[i,j])/3
            pix[i,j] = (p,p,p)

    return prueba


def work(im):
    w,h = im.size
    pixeles = im.load()
    matrix = zeros((w,h))

    for i in range(w):
        for j in range(h):
            matrix [i][j] = pixeles[i,j][1]

    
    columnas = matrix.sum(0) #Sumatoria de columnas
    filas = matrix.sum(1) #Sumatoria de filas

    umbral_f = (max(filas)-30050)
    umbral_c = (max(columnas)- 42000)

    candidatos = []

    for i in range(w):
        for j in range(h):
            if filas[i] < umbral_f and columnas[j] < umbral_c:
                candidatos.append([i,j])

    #Painting
    draw = ImageDraw.Draw(im)
    for elemento in candidatos:
        draw = ImageDraw.Draw(im)
        x = elemento[0]
        y = elemento[1]

        draw.line((x,0,x,h),fill=(255,0,0))
        draw.line((0,y,w,y),fill=(255,255,0))
    del draw


    im.show()


def main():
    im = Image.open('agujeros3.jpg')
    w,h = im.size
    pixeles = im.load()
    
    prueba = Image.new("RGB",(w,h))
    pix = prueba.load()

    gris = grises(im,w,h,pixeles,prueba,pix)    
    work(gris)
    #showing()

if __name__ == "__main__":
    main()
