# Importación de las librerias
import geopandas as gpd

# Importación información de los rios
rios = gpd.read_file("D:\Documentos\Jous\Ing-ud\Materias\2023-1\Programación\Final\Final-Programacion-II\Datos\Drenaje_doble_83IIIB.zip")
rios.plot(figsize=(12,12))