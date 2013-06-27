import math
import Image


def grises(ancho,altura,pixels,im):
    for j in range(altura):
        for i in range(ancho):
            prom = sum(pixels[i,j])/3
            pixels[i,j] = (prom,prom,prom)
    im.save('gris.png')
    #im.show()
    return im 

def convolucion(im):
    ancho,altura = im.size
    pixels = im.load()
    prom = 0                 ##declaraicon de variable para promedio
    suma = 0
    matrix = ([-1,0,1],[-2,0,2],[-1,0,1])
    matriy = ([1,2,1],[0,0,0],[-1,-2,-1])
    sumax = 0
    sumay = 0
    for j in range(altura):
        for i in range(ancho):
            sumax = 0
            sumay = 0
            for x in range(len(matrix[0])):
                for y in range(len(matrix[0])):
                    try:
                    #multix = matrix[x][y]*pixels[i+y -1,j+x -1][1]
                    #multiy = matriy[x][y]*pixels[i+y -1,j+x -1][1]
                        multix = matrix[x][y]*pixels[i+y,j+x][1]
                        multiy = matriy[x][y]*pixels[i+y,j+x][1]

                    except:
                        multix = 0
                        multiy = 0
                    sumax = multix + sumax
                    sumay = multiy + sumay
            xm = pow(sumax,2)
            ym = pow(sumay,2)
            g = int(math.sqrt(xm+ym))
            suma = g
        #suma = sumax + sumay
        #print suma
            if suma > 255:
                suma = 255
            if suma < 0:
                suma = 0
            pixels[i,j] = (suma,suma,suma)
    im.save('prueba.png')
    im.show()

def main():
    im = Image.open('mugrero.jpg')
    ancho,altura = im.size
    pixels = im.load()

    #gris = grises(ancho,altura,pixels,im)
    convolucion(im)

if __name__ == '__main__':
    main()
