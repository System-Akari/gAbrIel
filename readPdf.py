from PyPDF2 import PdfReader
import os

lector = PdfReader('prueba_merged.pdf') #creamos una variable que lea el archivo
nombre_doc_base = os.path.basename('prueba_merged.pdf') #extraemos el nombre del archivo con su extension
nombre_doc = os.path.splitext(nombre_doc_base)[0] + '.txt' #creamos un txt que se llame como el archivo original sin su extension
for i in range(len(lector.pages)): #ciclo for que recorre el archivo pdf pagina por pagina
    pagina = lector.pages[i] #extraemos el texto de la pagina 'i'

    #abrimos el archivo txt y escribimos el texto extraido con el lector y al final lo cerramos(buena practica)
    archivoN = open (nombre_doc,'a') 
    archivoN.write(pagina.extract_text()) 
    archivoN.close()

x = 'juan'
print ('Angelo estuvo aqui')