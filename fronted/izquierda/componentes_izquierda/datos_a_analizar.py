from dash import html
import dash_bootstrap_components as dbc

datos_a_analizar = dbc.Container(
    [
        html.H2('DATOS A ANALIZAR'),
        html.Hr(),
        html.Label('Centros Poblados'),
        dbc.Input(value='Población.shp'),
        html.Br(),
        dbc.Button('Subir', color='primary', className='mr-2'),
        html.Hr(),
        html.Label('Cartografía'),
        dbc.Input(value='Cartografía.shp'),
        html.Br(),
        dbc.Button('Subir', color='primary', className='mr-2'),
        html.Hr(),
        html.Label('Construcciones similares'),
        dbc.Input(value='Construcciones.shp'),
        html.Br(),
        dbc.Button('Subir', color='primary', className='mr-2'),
        html.Hr(),
        html.Label('Fuentes Hídricas'),
        dbc.Input(value='Aguas.shp'),
        html.Br(),
        dbc.Button('Subir', color='primary', className='mr-2'),
        html.Hr(),
        html.Label('Vías de acceso'),
        dbc.Input(value='Malla vial.shp'),
        html.Br(),
        dbc.Button('Subir', color='primary', className='mr-2'),
        html.Hr(),
    ]
)