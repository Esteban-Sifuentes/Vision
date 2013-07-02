import Image
import sys

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

def binarizacion(im,w,h,pixeles):
    nueva = Image.new("RGB",(w,h))
    new_pix = nueva.load()
    umbral = raw_input("Umbral de binarizacion: ")

    for j in range(h):
        for i in range(w):            
            if pixeles[i,j][1] < umbral:
                new_pix[i,j] = 0
            elif pixeles[i,j][1] >= umbral:
                new_pix[i,j] = 255

    nueva.save("binaria.png")
    nueva.show()
    return nueva

def main():
    im = Image.open('jenni.png')
    w,h = im.size
    pixeles = im.load()
    im.show()

    #contraste(im,w,h,pixeles)
    
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
        nueva.show()
        nueva = binarizacion(nueva,w,h,pixeles)
    
if __name__ == '__main__':
    main()
