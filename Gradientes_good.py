import math
import Image
from time import time
<<<<<<< HEAD
from math import floor
=======
>>>>>>> 6ebb7fce1eb8276bd283c8df126894773d03194e

Sobelx = ([-1,0,1],[-2,0,2],[-1,0,1])
Sobely = ([1,2,1],[0,0,0],[-1,-2,-1])


#Parametros: 
#dimensiones de la imagen (w,h)
#Arreglo de pixeles (pix)
#La imagen misma (im)

def grises(w,h,pix,im):
    t_inicial = time()
    #Recorremos el arreglo de pixeles
    for j in range(h):
        for i in range(w):
            #se suman los valores R,G,B
            #y se promedian al dividirlos entre 3
            prom = sum(pix[i,j])/3
            #el promedio es el nuevo valor de cada canal
            pix[i,j] = (prom,prom,prom)
    im.save('gris.png')
    #im.show()
<<<<<<< HEAD
    t_final = time()
=======
>>>>>>> 6ebb7fce1eb8276bd283c8df126894773d03194e
    t_total = t_final - t_inicial
    print "Tiempo en escala de grises: ",t_total
    return im 

def norm(normal):
    w,h = normal.size
    pixeles = normal.load()
    lista_pixeles = []
    lista_pixeles2= []
    for j in range(h):
        for i in range(w):
            pix = pixeles[i,j][1]
            lista_pixeles.append(pix)
    maximo = max(lista_pixeles)
    minimo = min(lista_pixeles)
    l = 255.0/(maximo-minimo)

    for j in range(h):
        for i in range(w):
            pix = pixeles[i,j][1]
            nuevo = int(floor((pix-minimo)*l))
            pixeles[i,j] = ((nuevo,nuevo,nuevo))
    normal.save('normal.png')
    #normal.show()                                                                                                                              
    return normal

def convolucion(im):
    t_inicial = time()
    w,h = im.size
    pix = im.load()
    prom = 0  
    suma = 0
    
    #Recorremos la imagen
    for j in range(h):
        for i in range(w):
            sumax = 0
            sumay = 0
<<<<<<< HEAD
	    #Recorremos la mascara
=======
        #Recorremos la mascara
>>>>>>> 6ebb7fce1eb8276bd283c8df126894773d03194e
            for x in range(len(Sobelx[0])):
                for y in range(len(Sobely[0])):
                    try:
			#Multiplicacion de valores
                        valorx = Sobelx[x][y]*pix[i+y,j+x][1]
                        valory = Sobely[x][y]*pix[i+y,j+x][1]

                    except:
                        valorx = 0
                        valory = 0
		    #Suma de multiplicaciones
                    sumax = valorx + sumax
                    sumay = valory + sumay
	    #Distancia euclidiana
            xm = pow(sumax,2)
            ym = pow(sumay,2)
            g = int(math.sqrt(xm+ym))
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            pix[i,j] = (g,g,g)
    im.save('prueba.png')
    #im.show()
    t_final = time()
    t_total = t_final - t_inicial

    print "Tiempo de convolucion: ",t_total
    return im

def binarizar(im):
    t_inicial = time()
    from sys import argv
    umbral = argv[1]

    w,h = im.size
    pixeles = im.load()
    for i in range(w):
        for j in range(h):
            if pixeles[i,j][1] < umbral:
                pixeles[i,j] = (0,0,0)
            else:
                pixeles[i,j] = (255,255,255)
    
    im.save('binaria.png')
    im.show()
    t_final = time()
    t_total = t_final - t_inicial
<<<<<<< HEAD
    print "Tiempo de binarizacion: ",t_total


def main():
    
    im = Image.open('jenni.png')
    #im = Image.open('mugrero.jpg')
=======
    print "Tiempo de convolucion: ",t_total

def main():
    im = Image.open('jenni.png')
>>>>>>> 6ebb7fce1eb8276bd283c8df126894773d03194e
    ancho,altura = im.size
    pixels = im.load()

    gris = grises(ancho,altura,pixels,im)
<<<<<<< HEAD
    normal = norm(gris)
    conv = convolucion(normal)
    binarizar(conv)
=======
    convolucion(gris)

>>>>>>> 6ebb7fce1eb8276bd283c8df126894773d03194e
if __name__ == '__main__':
    main()
