from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


#Creación container para la parte izquierda.
datos_a_analizar = dbc.Container(
    [
        html.H2('DATOS A ANALIZAR'),
        html.Hr(),
        #Creacion de label + botón carga para archivos .zip
        html.Label('Centros Poblados'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastre y suelte el archivo o ',
                html.A('Seleccione el archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
             },
             # Acepta archivos .zip
             accept='.zip'
         ),
        html.Hr(),
        html.Label('Construcciones similares'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastre y suelte el archivo o ',
                html.A('Seleccione el archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
             },
             # Acepta archivos .zip
             accept='.zip'
         ),
        html.Hr(),
        html.Label('Fuentes Hídricas'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastre y suelte el archivo o ',
                html.A('Seleccione el archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
             },
             # Acepta archivos .zip
             accept='.zip'
         ),
        html.Hr(),
        html.Label('Vías de acceso'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastre y suelte el archivo o ',
                html.A('Seleccione el archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
             },
             # Acepta archivos .zip
             accept='.zip'
         ),
        html.Hr(),
    ]
)