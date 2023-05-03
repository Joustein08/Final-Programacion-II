# Importación de las librerias
import geopandas as gpd
import matplotlib as plt

# Importación información de los rios
rios = gpd.read_file("D:/Documentos/Jous/Ing-ud/Materias/2023-1/Programación/Final/Final-Programacion-II/Datos/Drenaje_doble_83IIIB.zip")

rios["PROCESO"]="UNION"
rios_unidos = rios.dissolve('PROCESO')
rios_unidos["buffer1"] = rios_unidos.buffer(500)
rios_unidos["Categoria_1"] = (rios_unidos["buffer1"]-rios_unidos["geometry"])
rios_unidos["buffer2"] = rios_unidos.buffer(1000)
rios_unidos["Categoria_2"] = (rios_unidos["buffer2"]-rios_unidos["Categoria_1"]-rios_unidos["geometry"])
rios_unidos["buffer3"] = rios_unidos.buffer(4000)
rios_unidos["Categoria_3"] = (rios_unidos["buffer3"]-rios_unidos["Categoria_2"]-rios_unidos["Categoria_1"]-rios_unidos["geometry"])
limites = rios_unidos.total_bounds

# Grafica
categorias = rios_unidos["geometry"].plot(figsize = (12,12), alpha=0.5, color = "b")
rios_unidos["Categoria_1"].plot(ax = categorias, color = "r")
rios_unidos["Categoria_2"].plot(ax = categorias, color = "y")
rios_unidos["Categoria_3"].plot(ax = categorias, color = "g")


#rios.head(8)

categorias.set_xlim(limites[0],limites[2])
categorias.set_ylim(limites[1],limites[3])