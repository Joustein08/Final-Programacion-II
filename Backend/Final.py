# Importación de las librerias
import geopandas as gpd
import rasterio
from rasterio.features import rasterize
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from matplotlib.colors import ListedColormap
import io
import base64

# Ruta al archivo shapefile y a los archivos de salida raster
shapefile_path = 'Datos/Construccion_P.shp'
raster1_path = 'raster/Vias_3.tiff'
raster2_path  = 'raster/construcciones_3.tiff'
raster3_path = 'raster/Poblacion_3.tiff'
raster4_path  = 'raster/Rios_3.tiff'
output_path = 'raster/Final.tiff'

# Leer el archivo shapefile con GeoPandas
gdf = gpd.read_file(shapefile_path)

# Obtener los límites del shapefile original
bounds = gdf.total_bounds

# Definir el tamaño y resolución del raster
width, height = 1000, 1000
res = (bounds[2] - bounds[0]) / width

# Abrir los rasters de entrada
with rasterio.open(raster1_path) as src1, rasterio.open(raster2_path) as src2, rasterio.open(raster3_path) as src3, rasterio.open(raster4_path) as src4:
    # Leer los datos de los rasters de entrada
    raster1 = src1.read(1)
    raster2 = src2.read(1)
    raster3 = src3.read(1)
    raster4 = src4.read(1)

    # Realizar la resta de los rasters
    resultado = raster1 + raster2 + raster3 + raster4

    # Obtener los metadatos de uno de los rasters de entrada para usarlos en el raster de salida
    profile = src1.profile

    # Actualizar el tipo de dato y la cantidad de bandas del perfil para el raster de salida
    profile.update(dtype=rasterio.float32, count=1)

    # Guardar el raster de salida
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(resultado, 1)

    # Leer el archivo raster con Rasterio
    with rasterio.open(output_path) as src:
        raster = src.read(1)

# Definir los límites de los valores del raster para asignar los colores
vmin = np.min(raster)
vmax = np.max(raster)

# Definir la escala de colores personalizada
colors = ['red', 'yellow', 'green']
cmap = ListedColormap(colors)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize = (6,6))

# Mostrar el raster en los ejes utilizando la escala de colores personalizada
im = ax.imshow(raster, cmap=cmap, vmin=vmin, vmax=vmax)

# Agregar una barra de color
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
plt.colorbar(im, cax=cax)

# Establecer las etiquetas de los ejes utilizando el sistema de coordenadas del shapefile original
x_ticks = np.linspace(bounds[0], bounds[2], 5)
y_ticks = np.linspace(bounds[1], bounds[3], 5)
x_labels = [f'{x:.2f}' for x in x_ticks]
y_labels = [f'{y:.2f}' for y in y_ticks]
ax.set_xticks(np.linspace(0, width, len(x_ticks)))
ax.set_xticklabels(x_labels)
ax.set_yticks(np.linspace(0, height, len(y_ticks)))
ax.set_yticklabels(y_labels)

# Guardar la figura en un objeto BytesIO
figuraFinal = io.BytesIO()
plt.savefig(figuraFinal,format='png')
plt.close()

# Codificación de la imagen
Final_codificada = base64.b64encode(figuraFinal.getvalue()).decode()

# Calcular el histograma y porcentaje de influencia de cada raster
histograma1, bordes1 = np.histogram(raster1.flatten(), bins=256, range=[0, 255])
indice_color_predominante1 = np.argmax(histograma1)
porcentaje_influencia1 = (histograma1[indice_color_predominante1] / np.sum(histograma1)) * 100

histograma2, bordes2 = np.histogram(raster2.flatten(), bins=256, range=[0, 255])
indice_color_predominante2 = np.argmax(histograma2)
porcentaje_influencia2 = (histograma2[indice_color_predominante2] / np.sum(histograma2)) * 100

histograma3, bordes3 = np.histogram(raster3.flatten(), bins=256, range=[0, 255])
indice_color_predominante3 = np.argmax(histograma3)
porcentaje_influencia3 = (histograma3[indice_color_predominante3] / np.sum(histograma3)) * 100

histograma4, bordes4 = np.histogram(raster4.flatten(), bins=256, range=[0, 255])
indice_color_predominante4 = np.argmax(histograma4)
porcentaje_influencia4 = (histograma4[indice_color_predominante4] / np.sum(histograma4)) * 100

# Imprimir los porcentajes de influencia de cada archivo raster
print("Porcentaje de influencia de raster1: {:.0f}%".format(porcentaje_influencia1))
print(f"Porcentaje de influencia de raster2: {porcentaje_influencia2:.0f}%")
print(f"Porcentaje de influencia de raster3: {porcentaje_influencia3:.0f}%")
print(f"Porcentaje de influencia de raster4: {porcentaje_influencia4:.0f}%")