# Importamos las librerias necesarias 
import cv2
import pytesseract
import os

#Creamos funcion de OCR
def procesar_imagen(carpeta, archivo):
    ruta_archivo = os.path.join(carpeta, archivo)  # Obtenemos el archivo en una carpeta dada
    img = cv2.imread(ruta_archivo, cv2.IMREAD_GRAYSCALE) #Cargamos la imagen usando la libreria cv2
    threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Rescalamos la imagen y la pasamos a un tono de grises
    text = pytesseract.image_to_string(threshold_img) #Sacamos el texto de la imagen
    return text # retornamos el Texto

def imagenes_a_texto(carpeta):
    nombre_archivo = f'{os.path.basename(carpeta)}.txt' #Extreamos el nombre de la carpeta
    text_final = '' #en esta variable tendremos el texto extraido
    for archivo in os.listdir(carpeta):  #ingresamos a la carpeta y los archivos de la carpeta
        if archivo.endswith(('.webp', '.jpg', '.png')): #Solo leccionamos las imagenes 
            text = procesar_imagen(carpeta, archivo) #llamos a la funcion del OCR
            text_final = text + text_final 
            with open(nombre_archivo, 'w') as file: #Creamos el archivo y le insertamos el texto
                file.write(text)

imagenes_a_texto('img')
