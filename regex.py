import re
import pandas as pd
from PyPDF2 import PdfReader

rutaArchivo = 'Analisis Anual 2018 ETAS.pdf'
document = PdfReader(rutaArchivo)
pagina = document.pages[4]
texto = pagina.extract_text()
patron_fila = re.compile(
    r"^(\d+)\s+(\d+)\s+(.*?)\s+"
    r"(Intoxicación Alimentaria|Rotavirus|Enfermedad Diarreica|"
    r"Fiebre Tifoidea|Hepatitis A)\s+"
    r"(.*?)\s+(\d+)$"
)



# patron = r'\n(\w+\s*\w+\s*\w*)\s+(\d+)\s+(\d+.\d+)\s+(\d+)\s+(\d+.\d+)'

# datos = re.findall(patron, texto)
# print(datos)

# etas = pd.DataFrame(datos, columns=['Area de Salud', 'Casos 2017','Tasas 2017','Casos 2018','Tasas 2018'])
# print("\n", etas)

def normalizar_filas(texto):
        filas = []          # Lista donde guardaremos las filas completas
        fila_actual = ""    # Acumulador de texto para una fila

        for linea in texto.splitlines():
            linea = linea.strip()

            # Ignorar líneas vacías
            if not linea:
                continue

            # Agregar la línea actual a la fila en construcción
            fila_actual += " " + linea

            # Si la línea termina con un número, la fila está completa
            if re.search(r"\d+$", linea):
                filas.append(fila_actual.strip())
                fila_actual = ""  # Reiniciar para la siguiente fila

        return filas
    


def extraer_columnas(filas):
    datos = []  # Lista de tuplas con las columnas

    for fila in filas:
        coincidencia = patron_fila.match(fila)

        if coincidencia:
            datos.append(coincidencia.groups())
        else:
            # Si una fila no coincide, la mostramos para depuración
            print("Fila no reconocida:")
            print(fila)
            print("-" * 50)

    return datos

def main():
     #Normalizar filas
    filas_normalizadas = normalizar_filas(texto)

    print("FILAS NORMALIZADAS:")
    for f in filas_normalizadas:
        print(f)
    print("=" * 50)

    #Extraer columnas
    resultado = extraer_columnas(filas_normalizadas)

    print("COLUMNAS EXTRAÍDAS:")
    for r in resultado:
        print(r)
main()

