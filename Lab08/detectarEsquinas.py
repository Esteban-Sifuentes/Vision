from PIL import Image, ImageDraw
import sys



def detectarEsquinas(nueva,w,h):
        #pixeles en escala de grises
	grises = nueva.load()
	medias = []

	#Obtengo lista de vecinos en cada pixel
	for i in range(w):
		medias.append([])
		for j in range(h):
			vecinos = []
			for x in [-1,0,1]:
				for y in [-1,0,1]:
					if 0 <= i+x < w and 0 <= j+y < h:
						vecinos.append(grises[i+x,j+y][1])

			#Ordeno dicha lista
			vecinos.sort()
			indice = len(vecinos)/2

			#Obtengo la media correcta
			if len(vecinos) % 2 == 1:
				media = vecinos[indice]
			else:
				media = (vecinos[indice-1] + vecinos[indice])/2

			#Obtengo matriz de medias
			medias[i].append(media)

	#Recorro valores de medias y pixeles de la imagen original (gris)
	draw = ImageDraw.Draw(nueva)
	for i in range(w):
		for j in range(h):
			#para restar los pixeles de ambas
			dif = abs(grises[i,j][1] - medias[i][j])

			#Todo aquel que no sea 0, ES ESQUINA
			if dif > 27:
				draw.rectangle([(i,j),(i-3,j-3)],outline="blue")

	nueva.save('esquinas_triangle.png')
	#nueva.save('esquinas_star.png')


def escalaGrises(im,w,h,pixeles):
	gris = Image.new("RGB",(w,h))
	pix = gris.load()

	for i in range(w):
		for j in range(h):
			p = sum(pixeles[i,j])/3
			pix[i,j] = (p,p,p)
	return gris

def main():
	#im = Image.open("star.png")
	im = Image.open("triangle.png")
	w,h = im.size
	pixeles = im.load()

	
	nueva = escalaGrises(im,w,h,pixeles)
	nueva = detectarEsquinas(nueva,w,h)
		
if __name__ == "__main__":
	main()
