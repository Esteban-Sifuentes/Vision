from Tkinter import *
from PIL import ImageTk, Image, ImageDraw
from numpy import zeros,where
import sys

#Transforma la imagen en escala de grises
def grises(im,w,h,pixeles,prueba,pix):
    for i in range(w):
        for j in range(h):
            p = sum(pixeles[i,j])/3
            pix[i,j] = (p,p,p)
    return prueba,w,h,pix

#Se asegura que una interseccion [fila,columna] se un agujero
def isItAgujero(x,y,pixeles,im,opcion):
    mascara = [[1,1,1],[1,1,1],[1,1,1]]

    #Calculamos el promedio de vecinos del pixel [x,y] dado
    promedio = 0
    for i in range(-1,2):
        for j in range(-1,2):
            promedio += pixeles[x+i,y+i][1] * mascara[i+1][j+1]
    promedio /= 9

    #Para agujeros oscuros, comparamos con un umbral bajo
    if opcion == "o":
        if promedio < 10:
            #Si se encuentra un agujero, dibuja un cuadrado sobre el
            draw = ImageDraw.Draw(im)
            draw.rectangle([(x-4,y-4),(x+4,y+4)],outline="#fc1a0a")

    #Para agujeros claros comparamos con un umbral alto
    elif opcion == "c":
        if promedio > 155:
            #Si se encuentra un agujero, dibuja un cuadrado sobre el
            draw = ImageDraw.Draw(im)
            draw.rectangle([(x-4,y-4),(x+4,y+4)],outline="#fc1a0a")


def detect(im,w,h,pixeles,opcion):
    #Usamos matriz de zeros de numpy para copiar los valores de pixeles                                                                                                                                                                                                                                                             
    matrix = zeros((w,h))

    #Copiamos cada valor                                                                                                                                                                                                                                                                                                            
    for i in range(w):
        for j in range(h):
            matrix [i][j] = pixeles[i,j][1]

    columnas = matrix.sum(0) #Sumatoria de columnas                                                                                                                                                                                                                                                                                 
    filas = matrix.sum(1) #Sumatoria de filas                                                                                                                                                                                                                                                                                       

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                                                                                                                                                                                                                                                                            

    #Posibles lugares donde hay un agujero                                                                                                                                                                                                                                                                                          
    candidatos = []

    #Ciclo para agujeros oscuros                                                                                                                                                                                                                                                                                                    
    if opcion == "o":
        umbral = 10
        for i in range(1,w-1):
            for j in range(1,h-1):
                #Un agujero oscuro, va a dar los valores mas bajos de la imagen.                                                                                                                                                                                                                                                    
                #Entonces busco las intersecciones de [fila,columna] donde un pixel es mas bajo que sus vecinos inmediatos                                                                                                                                                                                                          
                if filas[i-1] > filas[i] < filas[i+1] and columnas[j-1] > columnas[j] < columnas[j+1]:
                    candidatos.append([i,j])

    #Ciclo para agujeros claros                                                                                                                                                                                                                                                                                                     
    elif opcion == "c":
        umbral = 155
        for i in range(1,w-1):
            for j in range(1,h-1):
                #Un agujero claro, va a dar los valores mas altos de la imagen                                                                                                                                                                                                                                                      
                #Entonces busco las intersecciones de [fila,columna] donde un pixel es mas alto que sus vecinos inmediatos                                                                                                                                                                                                          
                if filas[i-1] < filas[i] > filas[i+1] and columnas[j-1] < columnas[j] > columnas[j+1]:
                    candidatos.append([i,j])
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #Dibujo lineas en cada interseccion
    draw = ImageDraw.Draw(im)
    for elemento in candidatos:
        x = elemento[0]
        y = elemento[1]
        if opcion == 'o':
            if matrix[x][y] < 10:
                #Las lineas atraviesan toda la imagen                                                                                                                                    
                draw.line((x,0,x,h),fill=(0,240,0))
                draw.line((0,y,w,y),fill=(0,0,200))
                #Me aseguro de que la interseccion sea un agujero y no una sombra                                                                                                        
                isItAgujero(x,y,pixeles,im,opcion)
            else:
                pass

        if opcion == 'c':
            if matrix[x][y] > 155:
                #Las lineas atraviesan toda la imagen                                                                                                                                    
                draw.line((x,0,x,h),fill=(0,240,0))
                draw.line((0,y,w,y),fill=(0,0,200))
                #Me aseguro de que la interseccion sea un agujero y no una sombra                                                                                                        
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
         #im = Image.open('agujeros5.jpg')

    w,h = im.size
    pixeles = im.load()
    prueba = Image.new("RGB",(w,h))
    pix = prueba.load()

    #Trabajaremos sobre imagen en escala de grises
    gris,width,height,pix = grises(im,w,h,pixeles,prueba,pix)    

    #Hora de detectar agujeros
    detect(gris,width,height,pix,opcion)

if __name__ == "__main__":
    main()
