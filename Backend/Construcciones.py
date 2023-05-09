# Importación de las librerias
import geopandas as gpd
import matplotlib as plt
import io
import base64

def analisisConstrucciones(proximidadConstrucciones):

    # Definición de variables
    if proximidadConstrucciones == "si":

        # Importación información de los construcciones
        construcciones = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Construcciones_83IIIB.zip")

        #Creación de columnas en el geodataframe para el análisis
        construcciones["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
        construcciones_unidos = construcciones.dissolve('PROCESO') # Union de los elementos del archivo shp
        construcciones_unidos["buffer1"] = construcciones_unidos.buffer(500) # Creación primera zona
        construcciones_unidos["Categoria_1"] = (construcciones_unidos["buffer1"]-construcciones_unidos["geometry"]) # Delimitación primera zona
        construcciones_unidos["buffer2"] = construcciones_unidos.buffer(1000) # Creación segunda zona
        construcciones_unidos["Categoria_2"] = (construcciones_unidos["buffer2"]-construcciones_unidos["Categoria_1"]-construcciones_unidos["geometry"]) # Delimitación segunda zona
        construcciones_unidos["buffer3"] = construcciones_unidos.buffer(4000) # Creación tercera zona
        construcciones_unidos["Categoria_3"] = (construcciones_unidos["buffer3"]-construcciones_unidos["Categoria_2"]-construcciones_unidos["Categoria_1"]-construcciones_unidos["geometry"]) # Delimitación tercera zona

        # Gráfica
        categorias = construcciones_unidos["geometry"].plot(figsize = (12,12), alpha=0.5, color = "b") # Área del rio
        construcciones_unidos["Categoria_1"].plot(ax = categorias, color = "r") # Área de la primera categoria
        construcciones_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        construcciones_unidos["Categoria_3"].plot(ax = categorias, color = "g") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(construcciones_unidos.total_bounds[0],construcciones_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(construcciones_unidos.total_bounds[1],construcciones_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraConstrucciones = io.BytesIO()
        # plt.savefig(figuraConstrucciones, format='png')
        # plt.close()

        # Codificación de la imagen
        construcciones_codificada = base64.b64encode(figuraConstrucciones.getvalue()).decode()
    else: 
        # Importación información de los construcciones
        construcciones = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Construcciones_83IIIB.zip")

        #Creación de columnas en el geodataframe para el análisis
        construcciones["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
        construcciones_unidos = construcciones.dissolve('PROCESO') # Union de los elementos del archivo shp
        construcciones_unidos["buffer1"] = construcciones_unidos.buffer(500) # Creación primera zona
        construcciones_unidos["Categoria_1"] = (construcciones_unidos["buffer1"]-construcciones_unidos["geometry"]) # Delimitación primera zona
        construcciones_unidos["buffer2"] = construcciones_unidos.buffer(1000) # Creación segunda zona
        construcciones_unidos["Categoria_2"] = (construcciones_unidos["buffer2"]-construcciones_unidos["Categoria_1"]-construcciones_unidos["geometry"]) # Delimitación segunda zona
        construcciones_unidos["buffer3"] = construcciones_unidos.buffer(4000) # Creación tercera zona
        construcciones_unidos["Categoria_3"] = (construcciones_unidos["buffer3"]-construcciones_unidos["Categoria_2"]-construcciones_unidos["Categoria_1"]-construcciones_unidos["geometry"]) # Delimitación tercera zona

        # Gráfica
        categorias = construcciones_unidos["geometry"].plot(figsize = (12,12), alpha=0.5, color = "b") # Área del rio
        construcciones_unidos["Categoria_1"].plot(ax = categorias, color = "g") # Área de la primera categoria
        construcciones_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        construcciones_unidos["Categoria_3"].plot(ax = categorias, color = "r") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(construcciones_unidos.total_bounds[0],construcciones_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(construcciones_unidos.total_bounds[1],construcciones_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraConstrucciones = io.BytesIO()
        # plt.savefig(figuraConstrucciones, format='png')
        # plt.close()

        # Codificación de la imagen
        construcciones_codificada = base64.b64encode(figuraConstrucciones.getvalue()).decode() 
    
    # Crear la figura HTML con Dash
    return construcciones_codificada
