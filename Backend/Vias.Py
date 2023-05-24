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
shapefile_path = 'Datos/Via.shp'
raster1_path = 'raster/Vias_1.tiff'
raster2_path  = 'raster/Vias_2.tiff'
output_path = 'raster/Vias_3.tiff'

# Leer el archivo shapefile con GeoPandas
gdf = gpd.read_file(shapefile_path)

# Realizar un buffer de 500 unidades espaciales para la primera zona
buffer_distance_1 = 200
buffered_gdf_1 = gdf.copy()
buffered_gdf_1['geometry'] = buffered_gdf_1.buffer(buffer_distance_1)

# Realizar un buffer de 1000 unidades espaciales
buffer_distance_2 = 400
buffered_gdf_2 = gdf.copy()
buffered_gdf_2['geometry'] = buffered_gdf_2.buffer(buffer_distance_2)

# Obtener los límites del shapefile original
bounds = gdf.total_bounds

# Definir el tamaño y resolución del raster
width, height = 1000, 1000
res = (bounds[2] - bounds[0]) / width

# Agregar la columna 'buffer_value' al GeoDataFrame bufferizado y asignar el valor de esta categoría
buffered_gdf_1['buffer_value'] = 1

# Agregar la columna 'buffer_value' al GeoDataFrame bufferizado y asignar el valor de esta categoría
buffered_gdf_2['buffer_value'] = 2   

# Rasterizar el shapefile bufferizado para la primera categoria
arr_1 = rasterize([(geom, value) for geom, value in zip(buffered_gdf_1.geometry, buffered_gdf_1['buffer_value'])], out_shape=(height, width), transform=rasterio.Affine(res, 0, bounds[0], 0, -res, bounds[3]), dtype=np.uint8)

# Guardar el arreglo como archivo raster para la primera categoria
with rasterio.open(raster1_path, 'w', driver='GTiff', width=width, height=height, count=1, dtype=arr_1.dtype, crs=gdf.crs, transform=rasterio.Affine(res, 0, bounds[0], 0, -res, bounds[3])) as dst:dst.write(arr_1, 1)

# Rasterizar el shapefile bufferizado
arr_2 = rasterize([(geom, value) for geom, value in zip(buffered_gdf_2.geometry, buffered_gdf_2['buffer_value'])], out_shape=(height, width), transform=rasterio.Affine(res, 0, bounds[0], 0, -res, bounds[3]), dtype=np.uint8)

# Guardar el arreglo como archivo raster
with rasterio.open(raster2_path , 'w', driver='GTiff', width=width, height=height, count=1, dtype=arr_2.dtype, crs=gdf.crs, transform=rasterio.Affine(res, 0, bounds[0], 0, -res, bounds[3])) as dst:dst.write(arr_2, 1)

def analisisVias(proximidadVias):

    # Definición de variables
    if proximidadVias == "SI":

        # Abrir los rasters de entrada
        with rasterio.open(raster1_path) as src1, rasterio.open(raster2_path) as src2:
            # Leer los datos de los rasters de entrada
            raster1 = src1.read(1)
            raster2 = src2.read(1)

            # Realizar la resta de los rasters
            resultado = raster2 - raster1

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

        # Asignar valor de 1 al fondo del raster
        raster[raster == 0] = 3

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
        figuraVias = io.BytesIO()
        plt.savefig(figuraVias,format='png')
        plt.close()

        # Codificación de la imagen
        Vias_codificada = base64.b64encode(figuraVias.getvalue()).decode()
    
    elif proximidadVias == "NO": 

        # Abrir los rasters de entrada
        with rasterio.open(raster1_path) as src1, rasterio.open(raster2_path) as src2:
            # Leer los datos de los rasters de entrada
            raster1 = src1.read(1)
            raster2 = src2.read(1)

            # Realizar la resta de los rasters
            resultado = raster1 + raster2

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

        # Asignar valor de 1 al fondo del raster
        raster[raster == 0] = 1

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
        figuraVias = io.BytesIO()
        plt.savefig(figuraVias,format='png',)
        plt.close()

        # Codificación de la imagen
        Vias_codificada = base64.b64encode(figuraVias.getvalue()).decode()
        
    else:
        Vias_codificada = print("")
    
    # Crear la figura HTML con Dash
    return Vias_codificada