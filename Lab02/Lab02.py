import Image
from math import sqrt, pow



def grises(im,w,h,pixeles):
    gris = Image.new("RGB",(w,h))
    pix = gris.load()

    for j in range(h):
        for i in range(w):
            p = sum(pixeles[i,j])/3
            pix[i,j] = (p,p,p)
    #gris.show()
    return gris

def convolucion(im):
    w,h = im.size
    pixeles = im.load()

def main():
    im = Image.open('mugrero.jpg')
    w,h = im.size
    pixeles = im.load()

    cambio = grises(im,w,h,pixeles)
    cambio = convolucion(cambio)

if __name__ == '__main__':
    main()
