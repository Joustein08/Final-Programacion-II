# Importación de las librerias
import geopandas as gpd
import matplotlib as plt

# Importación información de los vias
vias = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/vias_83IIIB.zip")

#Creación de columnas en el geodataframe para el análisis
vias["PROCESO"]="UNION" # Creación de columna proceso para realizar la union de los elementos del archivo shp
vias_unidos = vias.dissolve('PROCESO') # Union de los elementos del archivo shp
vias_unidos["buffer1"] = vias_unidos.buffer(200) # Creación primera zona
vias_unidos["Categoria_1"] = (vias_unidos["buffer1"]-vias_unidos["geometry"]) # Delimitación primera zona
vias_unidos["buffer2"] = vias_unidos.buffer(400) # Creación segunda zona
vias_unidos["Categoria_2"] = (vias_unidos["buffer2"]-vias_unidos["Categoria_1"]-vias_unidos["geometry"]) # Delimitación segunda zona
vias_unidos["buffer3"] = vias_unidos.buffer(4000) # Creación tercera zona
vias_unidos["Categoria_3"] = (vias_unidos["buffer3"]-vias_unidos["Categoria_2"]-vias_unidos["Categoria_1"]-vias_unidos["geometry"]) # Delimitación tercera zona

# Gráfica
categorias = vias_unidos["geometry"].plot(figsize = (12,12), alpha=0.5, color = "b") # Área del rio
vias_unidos["Categoria_1"].plot(ax = categorias, color = "g") # Área de la primera categoria
vias_unidos["Categoria_2"].plot(ax = categorias, color = "y") # Área de la segunda categoria
vias_unidos["Categoria_3"].plot(ax = categorias, color = "r") # Área de la tercera categoria

# Delimitación gráfica
categorias.set_xlim(vias_unidos.total_bounds[0],vias_unidos.total_bounds[2]) # Eje x
categorias.set_ylim(vias_unidos.total_bounds[1],vias_unidos.total_bounds[3]) # Eje y