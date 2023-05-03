# Importación de las librerias
import geopandas as gpd
import matplotlib as plt

# Importación información de los rios
rios = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Drenaje_doble_83IIIB.zip")
rios["buffer1"] = rios.buffer(200)
rios["Categoria_1"] = (rios["buffer1"]-rios["geometry"])
rios["buffer2"] = rios.buffer(400)
rios["Categoria_2"] = (rios["buffer2"]-rios["Categoria_1"]-rios["geometry"])

# Grafica
categorias = rios["geometry"].plot(figsize = (12,12), alpha=0.5, color = "b")
rios["Categoria_1"].plot(ax = categorias, color = "r")
rios["Categoria_2"].plot(ax = categorias, color = "y")
rios.head(8)

# hola