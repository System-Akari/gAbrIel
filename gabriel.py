import tensorflow as tf
import nltk
from transformers import MarianMTModel, MarianTokenizer

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

# Cargar el modelo preentrenado y el tokenizador
model_name = 'Helsinki-NLP/opus-mt-en-es'  # Modelo de traducción de inglés a español
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Función para traducir texto de inglés a español
def translate(text):
    # Tokenización y generación de tokens de entrada
    tokens = tokenizer.encode(text, return_tensors='pt')
    
    # Traducción
    translated = model.generate(tokens, max_length=128, num_beams=4, early_stopping=True)
    
    # Decodificación de la traducción
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text


while True: 
    # Texto de ejemplo en inglés
    input_text = str(input('Ingrese el texto que desea traducir: '))
    if input_text == 'Salir':
        break
    else:
        # Traducción del texto al español
        translated_text = translate(input_text)

        # Imprimir la traducción
        print("English:", input_text)
        print("Spanish:", translated_text)


