from dash import html, dcc
import dash_bootstrap_components as dbc

definicion_proyecto = dbc.Container(
    [
        html.H2('DEFINICIÓN PROYECTO'),
        html.Hr(),
        html.Label('¿Al proyecto le afecta la proximidad con construcciones similares'),
        dcc.Dropdown(
            id = 'proximidadConstrucciones',
            options = ['si', 'no'],
        ),
    ]
)
