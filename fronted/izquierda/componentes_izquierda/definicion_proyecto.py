from dash import html, dcc
import dash_bootstrap_components as dbc

definicion_proyecto = dbc.Container(
    html.Div([
        html.H2('DEFINICIÓN PROYECTO'),
        html.Hr(),
        html.Label('¿Al proyecto le afecta la proximidad con construcciones similares?'),
        dcc.Dropdown(
            id='proximidadConstrucciones',
            options=[
                {'label': 'SI', 'value': 'SI'},
                {'label': 'NO', 'value': 'NO'}
            ],
        ),
        html.Br(),
        html.Label('¿Al proyecto le afecta la proximidad con drenajes, rios o cuerpos de agua?'),
        dcc.Dropdown(
            id='proximidadRios',
            options=[
                {'label': 'SI', 'value': 'SI'},
                {'label': 'NO', 'value': 'NO'}
            ],
        ),
        html.Br(),
        html.Label('¿Al proyecto le afecta la proximidad con centros poblados?'),
        dcc.Dropdown(
            id='proximidadPoblación',
            options=[
                {'label': 'SI', 'value': 'SI'},
                {'label': 'NO', 'value': 'NO'}
            ],
        ),
        html.Br(),
        html.Label('¿Es de interés para el proyecto al análisis de red vial?'),
        dcc.Dropdown(
            id='proximidadVias',
            options=[
                {'label': 'SI', 'value': 'SI'},
                {'label': 'NO', 'value': 'NO'}
            ],
        
        ),
        html.Br(),
        html.Table(id='tabla'),
    ]),
    
)
