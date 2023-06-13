from PyPDF2 import PdfReader
import os

#funcion para extraer el texto de un pdf
def pdf_a_txt(archivoPDF):
    lector = PdfReader(archivoPDF) #creamos una variable que lea el archivo
    nombre_doc_base = os.path.basename(archivoPDF) #extraemos el nombre del archivo con su extension
    nombre_doc = os.path.splitext(nombre_doc_base)[0] + '.txt' #creamos un txt que se llame como el archivo original sin su extension
    for i in range(len(lector.pages)): #ciclo for que recorre el archivo pdf pagina por pagina
        pagina = lector.pages[i] #extraemos el texto de la pagina 'i'

        #abrimos el archivo txt y escribimos el texto extraido con el lector y al final lo cerramos(buena practica)
        archivoN = open (nombre_doc,'a') 
        archivoN.write(pagina.extract_text()) 
        archivoN.close()
        
x = 'juan'
print ('Angelo estuvo aqui')

from fpdf import FPDF

#Esta funcion nos permite controla el proceso de compresion a PDF
def txt_a_pdf(archivo_txt, archivo_pdf):
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_auto_page_break(auto = True, margin = 15)
    pdf.set_font('Arial', size = 12)

#En este pequeño bloque nos permitira abrir el archivo de texto para su analisis
    with open(archivo_txt, 'r') as archivo:
        contenido = archivo.read()
    
    lineas = contenido.split('\n') #Aqui ira haciendo saltos de linea cuando el texto llege a los margenes definidos en la funcion

#Aqui irá comprimiendo en el PDF cada linea de archivo
    for linea in lineas:
        pdf.multi_cell(0, 10, txt = linea, align = 'L')
    
    pdf.output(archivo_pdf) #Comprime el archivo termiado en PDF
