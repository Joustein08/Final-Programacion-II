from dash import html
import dash_bootstrap_components as dbc

from .componentes_derecha.análisis_resultados_final import *
derecha = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(analisis_resultados_final, md=12,style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),   
            ]
        )
    ]
)