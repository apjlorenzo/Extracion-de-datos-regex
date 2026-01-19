import re
import pandas as pd
from PyPDF2 import PdfReader
import os
rutaArchivo = 'Analisis Anual 2018 ETAS.pdf'
document = PdfReader(rutaArchivo)
pagina = document.pages[2]
texto = pagina.extract_text()

patron = r'\n(\w+\s*\w+\s*\w*)\s+(\d+)\s+(\d+.\d+)\s+(\d+)\s+(\d+.\d+)'

datos = re.findall(patron, texto)
print(datos)

etas = pd.DataFrame(datos, columns=['Area de Salud', 'Casos 2017','Tasas 2017','Casos 2018','Tasas 2018'])
print("\n", etas)