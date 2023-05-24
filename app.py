# Importación de las librerias
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#IMPORTAR FRONTED
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda
from fronted.izquierda.componentes_izquierda.análisis_resultados_capa import asignar_color_porcentaje

#IMPORTAR BACKEND
from Backend.Construcciones import *
from Backend.Drenaje_Doble import *
from Backend.Poblacion import *
from Backend.Vias import *
from Backend.Final import porcentaje_influencia1, porcentaje_influencia2, porcentaje_influencia3, porcentaje_influencia4
from Backend.Final import Final_codificada

# Creación de la aplicación Dash
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definición del diseño de la aplicación
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),
                dbc.Col(izquierda, md=6, style={'text-align': 'center'}),
                dbc.Col(derecha, md=6, style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),
            ]
        )
    ]
)

# Callback para la función de análisis de construcciones similares
@app.callback(
    Output('salidaConstrucciones', 'children'),
    Input('proximidadConstrucciones', 'value')
)

# Definición de la función de análisis de construcciones similares, la cual muestra la imagen final de dicho análisis
def construcciones(proximidadConstrucciones):
    construcciones_codificada = analisisConstrucciones(proximidadConstrucciones)
    imagenConstrucciones = html.Img(src="data:image/png;base64,{}".format(construcciones_codificada))
    return html.Div([imagenConstrucciones])

# Callback para la función de análisis de rios
@app.callback(
    Output('salidaRios', 'children'),
    Input('proximidadRios', 'value')
)

# Definición de la función de análisis de rios, la cual muestra la imagen final de dicho análisis
def Rios(proximidadRios):
    rios_codificada = analisisRios(proximidadRios)
    imagenRios = html.Img(src="data:image/png;base64,{}".format(rios_codificada))
    return html.Div([imagenRios])

# Callback para la función de análisis de población
@app.callback(
    Output('salidaPoblacion', 'children'),
    Input('proximidadPoblacion', 'value')
)

# Definición de la función de análisis de población, la cual muestra la imagen final de dicho análisis
def Poblacion(proximidadPoblacion):
    Poblacion_codificada = analisisPoblacion(proximidadPoblacion)
    imagenPoblacion = html.Img(src="data:image/png;base64,{}".format(Poblacion_codificada))
    return html.Div([imagenPoblacion])

# Callback para la función de análisis de vías
@app.callback(
    Output('salidaVias', 'children'),
    Input('proximidadVias', 'value')
)

# Definición de la función de análisis de vías, la cual muestra la imagen final de dicho análisis
def Vias(proximidadVias):
    Vias_codificada = analisisVias(proximidadVias)
    imagenVias = html.Img(src="data:image/png;base64,{}".format(Vias_codificada))
    return html.Div([imagenVias])

# Callback para actualizar la tabla
@app.callback(
    Output('tabla', 'children'),
    Input('proximidadConstrucciones', 'value'),
    Input('proximidadRios', 'value'),
    Input('proximidadPoblacion', 'value'),
    Input('proximidadVias', 'value')
)

# Definición de la función para mostrar la validación de selección de las opciones en la definición del proyecto
def update_table(proximidad_construcciones, proximidad_rios, proximidad_poblacion, proximidad_vias):
    estilo_construcciones = {'background-color': 'green', 'fontWeight': 'bold', 'color': 'white', 'border': '1.75px solid black'}
    estilo_rios = {'background-color': 'green', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid black'}
    estilo_poblacion = {'background-color': 'green', 'fontWeight': 'bold', 'color': 'white', 'border': '1.75px solid black'}
    estilo_vias = {'background-color': 'green', 'fontWeight': 'bold', 'color': 'white', 'border': '1.75px solid black'}

    filas = [
        html.Tr([
            html.Td('_CONSTRUCCIONES_', style=estilo_construcciones if proximidad_construcciones == 'SI' else {}),
            html.Td('__FUENTES HÍDRICAS__', style=estilo_rios if proximidad_rios == 'SI' else {}),
            html.Td('__CENTROS POBLADOS__', style=estilo_poblacion if proximidad_poblacion == 'SI' else {}),
            html.Td('__RED VIAL_', style=estilo_vias if proximidad_vias == 'SI' else {}),
        ])
    ]
    return html.Table(filas)

# Callback para mostrar las salidas de los análisis anteriores
@app.callback(
    Output("salidas", "children"),
    Input("boton-mostrar-salidas", "n_clicks"),
    State('proximidadConstrucciones', 'value'),
    State('proximidadRios', 'value'),
    State('proximidadPoblacion', 'value'),
    State('proximidadVias', 'value')
)

# Definición del funcionamiento del botón para mostrar las gráficas de cada análisis
def mostrar_salidas(n_clicks, proximidad_construcciones, proximidad_rios, proximidad_poblacion,proximidad_Vias):
    if n_clicks:
        salida_construcciones = construcciones(proximidad_construcciones)
        salida_rios = Rios(proximidad_rios)
        salida_poblacion = Poblacion(proximidad_poblacion)
        salida_vias = Vias(proximidad_Vias)
        return html.Div([html.Hr(),
                         html.Label('ANÁLISIS DE CONSTRUCCIONES SIMILARES'),
                         html.Hr(),
                         salida_construcciones,
                         html.Hr(),
                         html.Label('ANÁLISIS DE FUENTES HÍDRICAS'),
                         html.Hr(),
                         salida_rios,
                         html.Hr(),
                         html.Label('ANÁLISIS DE CENTROS POBLADOS'),
                         html.Hr(),
                         salida_poblacion,
                         html.Hr(),
                         html.Label('ANÁLISIS DE RED VIAL'),
                         html.Hr(),
                         salida_vias])
    return html.Div()

# Callback para mostrar la imagen final
@app.callback(
    Output('salidaFinal', 'children'),
    Input('proximidadVias', 'value')
)

# Definición de la función para mostrar a imagen final
def Final():
    imagenFinal = html.Img(src="data:image/png;base64,{}".format(Final_codificada))
    return html.Div([imagenFinal])


# Callback para mostrar la gráfica final
@app.callback(
    Output("salidaGraficaFinal", "children"),
    Input("boton-mostrar-final", "n_clicks")
)

# Definición del funcionamiento del botón para mostrar la gráfica final
def mostrar_final(n_clicks):
    if n_clicks:
        salida_final= Final()
        return html.Div([html.Hr(),
                         salida_final,
                         html.Hr(),])
    return html.Div()


# Callback para mostrar la tabla de resultados_capa
@app.callback(
    Output('tabla-container', 'children'),
    [Input('boton-generar-tabla', 'n_clicks')]
)

# Definición del funcionamiento del botón para mostrar la tabla de resultados_capa
def generar_tabla(n_clicks):
    if n_clicks > 0:
        return dbc.Table(
            [
                html.Tr([
                    html.Td('CAPA', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                    html.Td('FACTIBILIDAD', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                ]),
                html.Tr([
                    html.Td('CONSTRUCCIONES SIMILARES', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td([
                        html.Div(style={'width': f'{round(porcentaje_influencia2, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia2), 'height': '20px'}),
                        html.Span(f'{round(porcentaje_influencia2, 2)}%')
                    ]),
                ]),
                html.Tr([
                    html.Td('FUENTES HÍDRICAS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td([
                        html.Div(style={'width': f'{round(porcentaje_influencia4, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia4), 'height': '20px'}),
                        html.Span(f'{round(porcentaje_influencia4, 2)}%')
                    ]),
                ]),
                html.Tr([
                    html.Td('CENTROS POBLADOS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td([
                        html.Div(style={'width': f'{round(porcentaje_influencia3, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia3), 'height': '20px'}),
                        html.Span(f'{round(porcentaje_influencia3, 2)}%')
                    ]),
                ]),
                html.Tr([
                    html.Td('RED VIAL', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td([
                        html.Div(style={'width': f'{round(porcentaje_influencia1, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia1), 'height': '20px'}),
                        html.Span(f'{round(porcentaje_influencia1, 2)}%')
                    ]),
                ]),
            ],
            style={'width': '100%'}
        )

# Iniciar el servidor Dash
if __name__ == '__main__':
    app.server.config['TIMEOUT'] = 180
    app.run_server(debug=True) 