from dash import html
import dash_bootstrap_components as dbc

from .componentes_izquierda.introduccion import introduccion
from .componentes_izquierda.definicion_proyecto import definicion_proyecto
from .componentes_izquierda.datos_a_analizar import datos_a_analizar
from .componentes_izquierda.convenciones import convenciones


izquierda = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(introduccion, md=12,style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),  
                dbc.Col(definicion_proyecto, md=12,style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),
                dbc.Col(datos_a_analizar, md=12,style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),
                dbc.Col(convenciones, md=12,style={'border': '2px solid black','padding': '10px','margin-bottom': '20px','text-align': 'center'}),
            ]
        )
    ]
)
