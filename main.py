import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect
from readPdf import pdf_a_txt, txt_a_pdf

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

# Cargar el modelo preentrenado y el tokenizador
model_name = 'Helsinki-NLP/opus-mt-en-es'  # Modelo de traducción de inglés a español
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)



def leer_archivo_txt(archivotx):
    lineas = []  # Array para almacenar las líneas del archivo
    with open(archivotx, 'r') as archivo:
        for linea in archivo:
            lineas.append(linea.strip())
    return lineas

    

#####tryyyyyyyyyy


# Función para traducir texto de un idioma a otro
def translate(archivo, source_lang, target_lang):
    lineas  = []
    if (r"\.txt$", archivo):
        lineas = leer_archivo_txt(archivo)    
    else: 
        print('no code')
    tokens = tokenizer.encode(archivo, return_tensors='pt')

    # Traducción
    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)

    # Decodificación de la traducción
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text

####try2
def translate1(file_path, source_lang, target_lang):
    if file_path.lower().endswith(".txt"):  # check if file has .txt extension
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file]  # use list comprehension to read lines

        tokens = tokenizer.encode(lines, return_tensors="pt")  # encode lines as tokens
    else:
        print("Not a text file")
        return ""

    translated = model.generate(tokens, max_length=911, num_beams=4, early_stopping=True)  # generate translation
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)  # decode translation

    return translated_text

def translate2(archivo, source_lang, target_lang):
    if archivo.endswith('.txt'):
        with open(archivo, 'r') as f:
            text = f.read()
    else: 
        print('Invalid file type')
        return 

    input_ids = tokenizer.encode(text, return_tensors='pt')
    translated = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text



def translate3(archivo, source_lang, target_lang):
    if (r"\.txt$", archivo):
        lineas = []  # Array para almacenar las líneas del archivo
        with open(archivo, 'r') as archivo:
            for linea in archivo:
                lineas.append(linea.strip())
                tokens = tokenizer.enconde(lineas, return_tensors='pt')
                translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)
                translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
                


    else: 
        print('no code')


    tokens = tokenizer.encode(archivo, return_tensors='pt')

    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)

    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text


while True:
    # Texto de entrada
    nombredoc = pdf_a_txt('Cinderella.pdf')
    print(translate1(nombredoc, 'en', 'es'))


# Funciones para ler un archivo y exportar un txt traducido
'''
archivo = open('cosas.txt')
contenido = archivo.read()

with open('cosas2.txt', 'w') as arc_final:
    arc_final.write(translate(contenido, 'en', 'es'))
'''