import Image
from math import sqrt, pow, floor


def guardar_bordes(lista_bordes,i,j,gx,gy,g):
    lista_bordes[(i,j)] = (gx,gy,g)    
    return lista_bordes

def grises(im,w,h,pixeles):
    gris = Image.new("RGB",(w,h))
    pix = gris.load()

    for j in range(h):
        for i in range(w):
            p = sum(pixeles[i,j])/3
            pix[i,j] = (p,p,p)
    #gris.show()
    return gris

def convolucion(im,mascara):
    w,h = im.size
    pixeles = im.load()
    copia = Image.new("RGB",(w,h))
    pix = copia.load()

    d = dict()
    for i in range(w):
        for j in range(h):
            res = 0
            gx = 0
            gy = 0

            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if 0 < x < w and 0 < y < h :
                        res += mascara[x - (i-1)][y - (j-1)] * pixeles[x,y][1]
                        #gy += mascaray[x - (i-1)][y - (j-1)] * pixeles[x,y][1]
                        #gx += mascara[x][y] * pixeles[i+y,j+x][1]
                        #gy += mascaray[x][y] * pixeles[i+y,j+x][1]
                    else:             
                        res = 0
            pix[i,j] = (res,res,res)
    return copia,pixeles

"""            g = int((gx**2 + gy**2)**0.5)
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            if 0 < g < 255:
                g = g

            pix[i,j] = (g,g,g)
            
            lista = guardar_bordes(d,i,j,gx,gy,g)

    return copia,lista
"""
def normalizacion(im):
    w,h = im.size
    pixeles = im.load()
    lista_pixeles = []

    normal = Image.new("RGB",(w,h))
    pixs = normal.load()
    
    for j in range(h):
        for i in range(w):
            pix = pixeles[i,j][0]
            lista_pixeles.append(pix)
    maximo = max(lista_pixeles)
    minimo = min(lista_pixeles)
    l = 255.0/(maximo-minimo)

    lista = []
    for j in range(h):
        for i in range(w):
            pix = pixeles[i,j][0]
            nuevo = int(floor((pix-minimo)*l))
            pixs[i,j] =(nuevo,nuevo, nuevo)
            lista.append(nuevo)

    return normal

def main():
    #im = Image.open('globo.jpg') #256 x 256
    #im = Image.open("moneda.jpg") #491 x 491
    im = Image.open('nah.jpg') #800 x 600
    w,h = im.size
    pixeles = im.load()
    print w,h
    im.show()

    #Mascaras de convolucion
    sobelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
    sobelY = [[1,2,1],[0,0,0],[-1,2,1]]

    prewittX = [[-1,0,1],[-1,0,1],[-1,0,1]]
    prewittY = [[1,1,1],[0,0,0],[-1,-1,-1]]

    #Filtros
    cambio = grises(im,w,h,pixeles)

    #cambio,resultado1 = convolucion(cambio,sobelX)
    #cambio,resultado2 = convolucion(cambio,sobelY)

    cambio,resultado1 = convolucion(cambio,prewittX)
    cambio,resultado1 = convolucion(cambio,prewittY)

    #cambio = normalizacion(cambio)
    
    cambio.show()

if __name__ == '__main__':
    main()
