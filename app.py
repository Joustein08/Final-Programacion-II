import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#IMPORTAR FRONTED
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

#IMPORTAR BACKEND
from Backend.Construcciones import *
from Backend.Drenaje_Doble import *

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

if __name__ == '__main__':
    app.run_server(debug=True) 