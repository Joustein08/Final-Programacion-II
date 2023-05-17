# Importación de las librerias
import geopandas as gpd
import matplotlib.pyplot as plt
import io
import base64

# Importación información de los rios
rios = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Drenaje_doble_83IIIB.zip")

#Creación de columnas en el geodataframe para el análisis
rios["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
rios_unidos = rios.dissolve('PROCESO') # Union de los elementos del archivo shp
rios_unidos["buffer1"] = rios_unidos.buffer(500) # Creación primera zona
rios_unidos["Categoria_1"] = (rios_unidos["buffer1"].difference(rios_unidos["geometry"])) # Delimitación primera zona
rios_unidos["buffer2"] = rios_unidos.buffer(1000) # Creación segunda zona
rios_unidos["Categoria_2"] = (rios_unidos["buffer2"].difference(rios_unidos["Categoria_1"]).difference(rios_unidos["geometry"])) # Delimitación segunda zona
rios_unidos["buffer3"] = rios_unidos.buffer(4000) # Creación tercera zona
rios_unidos["Categoria_3"] = (rios_unidos["buffer3"].difference(rios_unidos["Categoria_2"]).difference(rios_unidos["Categoria_1"]).difference(rios_unidos["geometry"])) # Delimitación tercera zona


def analisisRios(proximidadRios):
    # Definición de variables
    if proximidadRios == "SI":

        # Gráfica
        categorias = rios_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        rios_unidos["Categoria_1"].plot(ax = categorias, color = "r") # Área de la primera categoria
        rios_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        rios_unidos["Categoria_3"].plot(ax = categorias, color = "g") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(rios_unidos.total_bounds[0],rios_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(rios_unidos.total_bounds[1],rios_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraRios = io.BytesIO()
        plt.savefig(figuraRios, format='png')
        plt.close()
        # Codificación de la imagen
        rios_codificada = base64.b64encode(figuraRios.getvalue()).decode()
    elif proximidadRios == "NO": 

        # Gráfica
        categorias = rios_unidos["geometry"].plot(figsize = (6,6), alpha=0.5, color = "b") # Área del rio
        rios_unidos["Categoria_1"].plot(ax = categorias, color = "g") # Área de la primera categoria
        rios_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
        rios_unidos["Categoria_3"].plot(ax = categorias, color = "r") # Área de la tercera categoria

        # Delimitación gráfica
        categorias.set_xlim(rios_unidos.total_bounds[0],rios_unidos.total_bounds[2]) # Eje x
        categorias.set_ylim(rios_unidos.total_bounds[1],rios_unidos.total_bounds[3]) # Eje y

        # Guardar la figura en un objeto BytesIO
        figuraRios = io.BytesIO()
        plt.savefig(figuraRios, format='png')
        plt.close()

        # Codificación de la imagen
        rios_codificada = base64.b64encode(figuraRios.getvalue()).decode() 
    
    else:
        rios_codificada = print("")
    
    # Crear la figura HTML con Dash
    return rios_codificada
