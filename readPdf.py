from PyPDF2 import PdfReader

reader = PdfReader("prueba.pdf")
page = reader.pages[0]
prueba = open ('prueba.txt','w')
prueba.write(page.extract_text())
prueba.close()
''' 
    Agarrar todas las paginas
    Cree un archivo con el nombre del pdf
'''
x = 'juan'
print ('Angelo estuvo aqui')