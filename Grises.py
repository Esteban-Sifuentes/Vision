#Parametros: 
#dimensiones de la imagen (w,h)
#Arreglo de pixeles (pix)
#La imagen misma (im)

def grises(w,h,pix,im):
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
    return im 
