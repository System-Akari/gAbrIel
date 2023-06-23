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

def tomar_txt_traduccion(archivo):
    variable = ''
    nombre_doc_base = os.path.basename(archivo)
    nombre_doc = os.path.splitext(nombre_doc_base)[0] + '_es' +'.txt'
    newarchive = open(nombre_doc,'w')
    if (r"\.txt$", archivo):
        getext =  open(archivo)
        lines = getext.readlines()
        for i in lines:
            lane = i.split('\n')
            print(lane)
            translated_text = translate(lane ,'en','es')
            variable += translated_text
            print(variable)
            newarchive.write(variable)
    else: 
        print('no code')
    return ':D'


def translate(text, source_lang, target_lang):
    # Tokenización y generación de tokens de entrada
    tokens = tokenizer.encode(text, return_tensors='pt')

    # Traducción
    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)

    # Decodificación de la traducción
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text



tomar_txt_traduccion('Cinderella.txt')
    


# Funciones para ler un archivo y exportar un txt traducido
'''
archivo = open('cosas.txt')
contenido = archivo.read()

with open('cosas2.txt', 'w') as arc_final:
    arc_final.write(translate(contenido, 'en', 'es'))
'''