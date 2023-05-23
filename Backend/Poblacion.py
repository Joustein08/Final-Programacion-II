# Importación de las librerias
import geopandas as gpd
import matplotlib.pyplot as plt
import io
import base64

# Importación información de los poblacion
poblacion = gpd.read_file("Datos/Poblacion_83IIIB.zip")

#Creación de columnas en el geodataframe para el análisis
poblacion["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
poblacion_unidos = poblacion.dissolve('PROCESO') # Union de los elementos del archivo shp
poblacion_unidos["buffer1"] = poblacion_unidos.buffer(500) # Creación primera zona
poblacion_unidos["Categoria_1"] = poblacion_unidos["buffer1"].difference(poblacion_unidos["geometry"]) # Delimitación primera zona
poblacion_unidos["buffer2"] = poblacion_unidos.buffer(1000) # Creación segunda zona
poblacion_unidos["Categoria_2"] = poblacion_unidos["buffer2"].difference(poblacion_unidos["Categoria_1"]).difference(poblacion_unidos["geometry"]) # Delimitación segunda zona
poblacion_unidos["buffer3"] = poblacion_unidos.buffer(4000) # Creación tercera zona
poblacion_unidos["Categoria_3"] = poblacion_unidos["buffer3"].difference(poblacion_unidos["Categoria_2"]).difference(poblacion_unidos["Categoria_1"]).difference(poblacion_unidos["geometry"]) # Delimitación tercera zona


def analisisPoblacion(proximidadPoblacion):
    # Definición de variables
    if proximidadPoblacion == "SI":
        # Gráfica
        categorias = poblacion_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        poblacion_unidos["Categoria_1"].plot(ax = categorias, color = "r") # Área de la primera categoria
        poblacion_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        poblacion_unidos["Categoria_3"].plot(ax = categorias, color = "g") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(poblacion_unidos.total_bounds[0],poblacion_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(poblacion_unidos.total_bounds[1],poblacion_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraPoblacion = io.BytesIO()
        plt.savefig(figuraPoblacion, format='png')
        plt.close()

        # Codificación de la imagen
        poblacion_codificada = base64.b64encode(figuraPoblacion.getvalue()).decode()

    elif proximidadPoblacion == "NO":
        
        # Gráfica
        categorias = poblacion_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        poblacion_unidos["Categoria_1"].plot(ax = categorias, color = "g") # Área de la primera categoria
        poblacion_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        poblacion_unidos["Categoria_3"].plot(ax = categorias, color = "r") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(poblacion_unidos.total_bounds[0],poblacion_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(poblacion_unidos.total_bounds[1],poblacion_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraPoblacion = io.BytesIO()
        plt.savefig(figuraPoblacion, format='png')
        plt.close()

        # Codificación de la imagen
        poblacion_codificada = base64.b64encode(figuraPoblacion.getvalue()).decode()
    else:
        poblacion_codificada = print("")
    
    # Crear la figura HTML con Dash
    return poblacion_codificada