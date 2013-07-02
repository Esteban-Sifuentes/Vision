import Image
import sys
from math import floor, sqrt

def invertir(im,w,h,pixeles):
    invertida = Image.new("RGB",(w,h))
    new_pix = invertida.load()

    for j in range(h):
        for i in range(w):
            r,g,b = pixeles[i,j]
            new_pix[i,j] = (255-r,255-g,255-b)
    invertida.save('invertida.png')
    #invertida.show()
    return invertida
    

def tono(im,w,h,pixeles,canal):    
    nueva = Image.new("RGB",(w,h))
    new_pix = nueva.load()

    #canal = raw_input("Canal: ")
    for j in range(h):
        for i in range(w):
            r,g,b = pixeles[i,j]

            if canal == 'r':
                new_pix[i,j] = (r,0,0)
            elif canal == 'g':
                new_pix[i,j] = (0,g,0)
            elif canal == 'b':
                new_pix[i,j] = (0,0,b)
                
    nueva.save('tono.png')
    return nueva

def grises(im,w,h,pixeles):
    nueva = Image.new("RGB",(w,h))
    new_pix = nueva.load()
    for j in range(h):
        for i in range(w):
            p = sum(pixeles[i,j])/3
            new_pix[i,j] = (p,p,p)
    nueva.save('gris.png')
    #nueva.show()
    return nueva

def norm(normal):
    w,h = normal.size
    pixeles = normal.load()
    lista_pixeles = []
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
    return normal,pixeles


def binarizacion(im,w,h):
    pix = im.load()
    nueva = Image.new("RGB",(w,h))
    new_pix = nueva.load()
    umbral_min = 85
    umbral_max = 170

    for j in range(h):
        for i in range(w):
            if pix[i,j][1] > umbral_max:
                new_pix[i,j] = (255,255,255)
            elif pix[i,j][1] < umbral_min:
                new_pix[i,j] = (0,0,0)

    nueva.save("binaria.png")
    nueva.show()
    return nueva,new_pix

def convolucion(im):
    #im = Image.open("normal.png")
    width, height = im.size
    pix = im.load()
    resultado = 0
    gradienteX = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])  #Valores establecidos por medio del operador Sobel
    gradienteY = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])  #Para gradiente de y, el de arriba es el gradiente de x.
    sumasX = 0
    sumasY = 0 

    for x in range(height):
        for y in range(width):
            sumasX = 0
            sumasY = 0
            if x != 0 and y != 0 and y != width and x != height:
                for a in range(3): #Debido a que la matriz de los gradientes es de 3x3
                    for b in range(3):
                        try:
                            productosGX = gradienteX[a][b]*pix[y+b, x+a][1] #Obteniendo el valor de gradiente X
                            productosGY = gradienteY[a][b]*pix[y+b, x+a][1]#Obteniendo el valor de gradiente Y
                            
                        except:
                            productosGX = 0
                            productosGY = 0

                        sumasX = productosGX+sumasX #Adicionando los valores del gradiente X
                        sumasY = productosGY+sumasY #Adicionando los valores del gradiente Y

                potenciaGradienteX = pow(sumasX, 2) #Obteniendo el cuadrado del gradiente X
                potenciaGradienteY = pow(sumasY, 2) #Obteniendo el cuadrado del gradiente Y
                Gradiente = int(sqrt(potenciaGradienteX+potenciaGradienteY)) #Para obtener el gradiente por medio de los componentes x, y


                if Gradiente > 255: #Por si se pasan los valores
                    Gradiente = 255
                    
                if Gradiente < 0: #Para estar dentro del rango (0, 255) 
                    Gradiente = 0

                pix[y,x] = (Gradiente, Gradiente, Gradiente) # Creando el pixel nuevo con el gradiente obtenido

    im.save('convo.png')
    return im


def main():
    im = Image.open('mugrero.jpg')
    #im = Image.open('jenni.png')
    w,h = im.size
    pixeles = im.load()
    im.show()

    #contraste(im,w,h,pixeles)
    SobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    SobelY = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

    filtro = raw_input("Que hago? [i/t/q/g/c]")
                
    if filtro == 'i':
        nueva = invertir(im,w,h,pixeles)
        nueva.show()
    elif filtro == 't':
        canal = raw_input('Canal: [r/g/b]')
        nueva = tono(im,w,h,pixeles,canal)
        nueva.show()
    elif filtro == 'c':
        nueva = contraste(im,w,h,pixeles)
    elif filtro == 'g':
        nueva = grises(im,w,h,pixeles)
        #nueva,pixeles = binarizacion(nueva,w,h)
        nueva,pixeles = norm(nueva)
        nueva = convolucion(nueva)
        nueva.show()

if __name__ == '__main__':
    main()
