# Importación de las librerias
import geopandas as gpd
import matplotlib.pyplot  as plt
import io
import base64

def analisisConstrucciones(proximidadConstrucciones):

    # Importación información de los construcciones
    construcciones = gpd.read_file("Datos/Construcciones_83IIIB.zip")

    #Creación de columnas en el geodataframe para el análisis
    construcciones["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
    construcciones_unidos = construcciones.dissolve('PROCESO') # Union de los elementos del archivo shp
    construcciones_unidos["buffer1"] = construcciones_unidos.buffer(500) # Creación primera zona
    construcciones_unidos["Categoria_1"] = construcciones_unidos["buffer1"].difference(construcciones_unidos["geometry"]) # Delimitación primera zona
    construcciones_unidos["buffer2"] = construcciones_unidos.buffer(1000) # Creación segunda zona
    construcciones_unidos["Categoria_2"] = construcciones_unidos["buffer2"].difference(construcciones_unidos["Categoria_1"]).difference(construcciones_unidos["geometry"]) # Delimitación segunda zona
    construcciones_unidos["buffer3"] = construcciones_unidos.buffer(4000) # Creación tercera zona
    construcciones_unidos["Categoria_3"] = construcciones_unidos["buffer3"].difference(construcciones_unidos["Categoria_2"]).difference(construcciones_unidos["Categoria_1"]).difference(construcciones_unidos["geometry"]) # Delimitación tercera zona

    # Definición de variables
    if proximidadConstrucciones == "SI":

        # Gráfica
        categorias = construcciones_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        construcciones_unidos["Categoria_1"].plot(ax = categorias, color = "r") # Área de la primera categoria
        construcciones_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        construcciones_unidos["Categoria_3"].plot(ax = categorias, color = "g") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(construcciones_unidos.total_bounds[0],construcciones_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(construcciones_unidos.total_bounds[1],construcciones_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraConstrucciones = io.BytesIO()
        plt.savefig(figuraConstrucciones, format='png')
        plt.close()

        # Codificación de la imagen
        construcciones_codificada = base64.b64encode(figuraConstrucciones.getvalue()).decode()
    
    elif proximidadConstrucciones == "NO": 
        
        # Gráfica
        categorias = construcciones_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        construcciones_unidos["Categoria_1"].plot(ax = categorias, color = "g") # Área de la primera categoria
        construcciones_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        construcciones_unidos["Categoria_3"].plot(ax = categorias, color = "r") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(construcciones_unidos.total_bounds[0],construcciones_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(construcciones_unidos.total_bounds[1],construcciones_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraConstrucciones = io.BytesIO()
        plt.savefig(figuraConstrucciones, format='png')
        plt.close()

        # Codificación de la imagen
        construcciones_codificada = base64.b64encode(figuraConstrucciones.getvalue()).decode() 
    else:
        construcciones_codificada = print("")
    
    # Crear la figura HTML con Dash
    return construcciones_codificada
