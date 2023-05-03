# Importación de las librerias
import geopandas as gpd
import matplotlib as plt

# Importación información de los rios
rios = gpd.read_file("Datos\Drenaje_doble_83IIIB\Drenaje_Doble.shp")
rios.plot()