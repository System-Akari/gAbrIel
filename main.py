import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
from readPdf import pdf_a_txt, txt_a_pdf
import os


# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

# Cargar el modelo preentrenado y el tokenizador
model_name = 'Helsinki-NLP/opus-mt-en-es'  # Modelo de traducción de inglés a español
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

#Esta funcion toma el archivo txt y se lo entrega a la funcion de traduccion para devolver un nuevo archivo en espaniol
def tomar_txt_traduccion(archivo): 
    nombre_doc_base = os.path.basename(archivo) #tomamos el nombre base para el nombre del nuevo archivo
    nombre_doc = os.path.splitext(nombre_doc_base)[0] + '_es' +'.txt' #nombramos el nuevo archivo agregando un _es
    getext =  open(archivo, 'r') #Al no necesitar directamente el archivo nuevo, abrimos nuestro archivo base 
    lines = getext.readlines() #Obtenemos las lineas del documento
    #Hacemos un for para recorrer cada una de las lineas de nuestro documento
    for i in lines: 
        #tomamos la linea actual y la pasamos a nuestro traductor, y especificamos el lenguaje actual y el objetivo
        translated_text = translate(i,'en','es') 

        # Creamos el nuevo documento, escribimos la linea ya traducida con un contrapleca y lo cerramos
        newarchive = open(nombre_doc,'a')
        newarchive.write(translated_text + '\n')
        newarchive.close()
    #retornamos el nombre de nuestro nuevo documento para posteriormente     
    return nombre_doc


def translate(text, source_lang, target_lang):
    # Tokenización y generación de tokens de entrada
    tokens = tokenizer.encode(text, return_tensors='pt')

    # Traducción
    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)

    # Decodificación de la traducción
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text


# Aqui probamos nuestras funciones, donde a  pdf_a_txt 
# le pasaremos nuestro archivo y nos retornara el nombre del archivo txt 
nombre = pdf_a_txt('1952.pdf')

# lo mandamos a la funcion de extraer el txt y regresar un archivo nuevo ya traducido
nombre1 = tomar_txt_traduccion(nombre)
# Aca tomamos y generamos un nombre para el archivo final, en donde eliminamos la extension de .txt y agregamos la extension .pdf
nombre2 = nombre1[:-4] + '.pdf'
print(nombre2)

# Finalmente agregamos ambos archivos para que se envien finalmente
txt_a_pdf(nombre1, nombre2)



# Funciones para ler un archivo y exportar un txt traducido
'''
archivo = open('cosas.txt')
contenido = archivo.read()

with open('cosas2.txt', 'w') as arc_final:
    arc_final.write(translate(contenido, 'en', 'es'))
'''