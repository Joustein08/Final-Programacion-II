# Importación de las librerias
import geopandas as gpd
import matplotlib as plt

# Importación información de los rios
rios = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Drenaje_doble_83IIIB.zip")

rios["buffer"] = rios.buffer(50)
rios["buffer"].plot(figsize = (12,12))

# hola