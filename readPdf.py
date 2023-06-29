from PyPDF2 import PdfReader
import os


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
    return nombre_doc
        
def pdf_a_txt1(archivoPDF):
    lector = PdfReader(archivoPDF) #creamos una variable que lea el archivo
    nombre_doc_base = os.path.basename(archivoPDF) #extraemos el nombre del archivo con su extension
    nombre_doc = os.path.splitext(nombre_doc_base)[0] + '.txt' #creamos un txt que se llame como el archivo original sin su extension
    for i in range(len(lector.pages)): #ciclo for que recorre el archivo pdf pagina por pagina
        pagina = lector.pages[i] #extraemos el texto de la pagina 'i'
        if 'XObject' in pagina.keys() and any('/Im' in xobj for xobj in pagina['/XObject'].keys()):            
            continue  # Saltar la página si contiene imágenes
        
        # Extraer el texto de la página
        texto = pagina.extract_text()
        
        # Verificar si el texto está vacío
        if texto.strip():
            #abrimos el archivo txt y escribimos el texto extraido con el lector y al final lo cerramos(buena practica)
            archivoN = open (nombre_doc,'a') 
            archivoN.write(pagina.extract_text()) 
            archivoN.close()
    return nombre_doc
        



from fpdf import FPDF

#Esta funcion nos permite controla el proceso de compresion a PDF
def txt_a_pdf(archivo_txt, archivo_pdf): #Aquí le pasamos 2 parametros, el archivo que entra y el otro que sale
    pdf = FPDF() #Se declara la variable pdf para evitar estar llamando la función a cada rato
    pdf.add_page() #Nos añade una nueva paágina en blanco
    pdf.set_auto_page_break(auto = True, margin = 15) #Nos permite controlar los altos de línea y en que margen debe hacerlos
    pdf.set_font('Arial', size = 12) #Nos permite controlar el tamaño y fuente de página

#En este pequeño bloque nos permitira abrir el archivo de texto para su analisis
    with open(archivo_txt, 'r', encoding='utf-8') as archivo: #Abre el archivo y lo pone en modo lectura
        contenido = archivo.read() #Aquí guarda todo lo que se analizó en la variable contenido
    
    lineas = contenido.split('\n') #Aqui ira haciendo saltos de linea cuando el texto llege a los margenes definidos en la funcion

#Aqui irá comprimiendo en el PDF cada linea de archivo
    for linea in lineas:
        pdf.multi_cell(200, 10, txt=linea.encode('latin-1', 'replace').decode('latin-1'), align = 'L') #Aquí ajustamos los margenes de la hoja y el tipo de centrado y se riá repitiendo hasta que termine
    
    pdf.output(archivo_pdf) #Comprime el archivo terminado en PDF
    archivo_final = os.path.basename(archivo_pdf)
    return archivo_final
