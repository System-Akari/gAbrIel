# Importamos las librerias necesarias 
from pdf2image import convert_from_path
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

<<<<<<< HEAD
=======


#Direccion del conversor localmente
poppler_path = r"/usr/bin"

#Direccion del archivo a convertir (PDF)
pdf_path = r"./PDF de prueba.pdf"

#Procedemos a obtener las paginas del PDF (Los resultados)
pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path)


#Fucion para crear y nombrar el directorio
def creation_directory(pdf_path):

    # Quitarle la extencion al archivo del PATH que le pasamos
    directory_name= os.path.splitext(os.path.basename(pdf_path))[0]

    # Crear el directorio
    os.makedirs(directory_name)

    return directory_name


#Se crea una variable para enviar los archivos recien convertidos
saving_folder = creation_directory(pdf_path)


#Funcion para nombrar las imagenes
def name_images(pages, saving_folder):
    #Se crea una variable contador para nombrar los resultados
    image_counter = 1

    #Procedemos a recorer las imagenes nombrandolas
    for page in pages:
        image_name = f"img-{image_counter}.jpeg"
        page.save(os.path.join(saving_folder, image_name), "JPEG")
        image_counter += 1
    













>>>>>>> 48f8508 (Finalizacion del ocr)
