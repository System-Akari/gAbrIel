import tensorflow as tf
import nltk
from nltk.tokenize import word_tokenize
from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

# Cargar el modelo preentrenado y el tokenizador
model_name = 'Helsinki-NLP/opus-mt-en-es'  # Modelo de traducción de inglés a español
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


#Vamos a tokenizar utilizando la funcion generada anteriormente:

# Función para traducir texto de un idioma a otro
def translate(text, source_lang, target_lang):
    # Tokenización y generación de tokens de entrada
    tokens = tokenizer.encode(text, return_tensors='pt')

    # Traducción
    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)

    # Decodificación de la traducción
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text


while True:
    # Texto de entrada
    input_text = str(input('Ingrese el texto que desea traducir (o escriba "Salir" para salir): '))
    if input_text == 'Salir':
        break
    else:
        translated_text = translate(input_text, 'en', 'es')
        print("English:", input_text)
        print("Spanish:", translated_text)


# Funciones para ler un archivo y exportar un txt traducido
'''
archivo = open('cosas.txt')
contenido = archivo.read()

with open('cosas2.txt', 'w') as arc_final:
    arc_final.write(translate(contenido, 'en', 'es'))
'''