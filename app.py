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
    Input('proximidad', 'value')
)
def construcciones(proximidad):
    construcciones_codificada = analisisConstrucciones(proximidad)
    imagenConstrucciones = html.Img(src="data:image/png;base64,{}".format(construcciones_codificada))
    return html.Div([imagenConstrucciones])

if __name__ == '__main__':
    app.run_server(debug=True)