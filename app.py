import dash
from dash import html
import dash_bootstrap_components as dbc

#IMPORTAR FRONTED
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

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



if __name__ == '__main__':
    app.run_server(debug=True)