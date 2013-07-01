import Image
from math import floor
from math import pow, sqrt


def grises(im):
    gris = im.copy()
    w,h = gris.size
    pixeles = gris.load()
    for i in range(w):
        for j in range(h):
            prom = sum(pixeles[i,j])/3
            pixeles[i,j] = (prom,prom,prom)

    gris.save('gris.png')
    return gris

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


def convolucion(imagen_original, mascara):
    x, y = imagen_original.size
    pos = imagen_original.load()
    nueva_imagen = Image.new("RGB", (x,y))
    pos_nueva = nueva_imagen.load() 
    for i in range(x):
        for j in range(y):
            total = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and m >= 0 and n < x and m < y:
                        total += mascara[n - (i - 1)][ m - (j - 1)] * pos[n, m][0]
            pos_nueva[i, j] = (total, total, total)
    #nueva_imagen.save("mascara.png")
    return nueva_imagen


def main():
    im = Image.open('mugrero.jpg')
    SobelX = [[-1,0,1],[-2,0,2],[-1,0,1]]
    SobelY = [[1,2,1],[0,0,0],[-1,-2,-1]]



    gris = grises(im)
    normalizada = norm(gris)
    nueva = convolucion(normalizada, SobelX)
    nueva.save("mascara1.png")
    nueva = convolucion(nueva, SobelY)
    nueva.save("mascara2.png")
    nueva.show()

if __name__ == '__main__':
    main()
