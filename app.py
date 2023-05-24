import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#IMPORTAR FRONTED
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

#IMPORTAR BACKEND
from Backend.Construcciones import *
from Backend.Drenaje_Doble import *
from Backend.Poblacion import *
from Backend.Vias import *

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

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


@app.callback(
    Output('salidaConstrucciones', 'children'),
    Input('proximidadConstrucciones', 'value')
)
def construcciones(proximidadConstrucciones):
    construcciones_codificada = analisisConstrucciones(proximidadConstrucciones)
    imagenConstrucciones = html.Img(src="data:image/png;base64,{}".format(construcciones_codificada))
    return html.Div([imagenConstrucciones])

@app.callback(
    Output('salidaRios', 'children'),
    Input('proximidadRios', 'value')
)

def Rios(proximidadRios):
    rios_codificada = analisisRios(proximidadRios)
    imagenRios = html.Img(src="data:image/png;base64,{}".format(rios_codificada))
    return html.Div([imagenRios])

@app.callback(
    Output('salidaPoblacion', 'children'),
    Input('proximidadPoblacion', 'value')
)

def Poblacion(proximidadPoblacion):
    Poblacion_codificada = analisisPoblacion(proximidadPoblacion)
    imagenPoblacion = html.Img(src="data:image/png;base64,{}".format(Poblacion_codificada))
    return html.Div([imagenPoblacion])

@app.callback(
    Output('salidaVias', 'children'),
    Input('proximidadVias', 'value')
)

def Vias(proximidadVias):
    Vias_codificada = analisisVias(proximidadVias)
    imagenVias = html.Img(src="data:image/png;base64,{}".format(Vias_codificada))
    return html.Div([imagenVias])

@app.callback(
    Output('tabla', 'children'),
    Input('proximidadConstrucciones', 'value'),
    Input('proximidadRios', 'value'),
    Input('proximidadPoblacion', 'value'),
    Input('proximidadVias', 'value')
)
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
@app.callback(
    Output("salidas", "children"),
    Input("boton-mostrar-salidas", "n_clicks"),
    State('proximidadConstrucciones', 'value'),
    State('proximidadRios', 'value'),
    State('proximidadPoblacion', 'value'),
    State('proximidadVias', 'value')
)
def mostrar_salidas(n_clicks, proximidad_construcciones, proximidad_rios, proximidad_poblacion,proximidad_Vias):
    if n_clicks:
        salida_construcciones = construcciones(proximidad_construcciones)
        salida_rios = Rios(proximidad_rios)
        salida_poblacion = Poblacion(proximidad_poblacion)
        salida_vias = Vias(proximidad_Vias)
        return html.Div([html.Hr(),
                         html.Label('Análisis de construcciones similares'),
                         html.Hr(),
                         salida_construcciones,
                         html.Hr(),
                         html.Label('Análisis de cuerpos de agua'),
                         html.Hr(),
                         salida_rios,
                         html.Hr(),
                         html.Label('Análisis de cercanía de población'),
                         html.Hr(),
                         salida_poblacion,
                         html.Hr(),
                         html.Label('Análisis de cercanía de población'),
                         html.Hr(),
                         salida_vias])
    return html.Div()

if __name__ == '__main__':
    app.server.config['TIMEOUT'] = 60
    app.run_server(debug=True) 