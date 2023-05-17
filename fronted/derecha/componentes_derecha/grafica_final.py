from dash import html
import dash_bootstrap_components as dbc

grafica_final = dbc.Container(
    [
        html.H2('GRÁFICA FINAL'),
        html.Hr(),
        html.Img(src='fronted/derecha/componentes_derecha/Ubicacion.png', style={'width': '500px', 'height': '300px'}),
        html.Br(),
        dbc.Button('Descargar', color='primary', className='mr-2'),
        html.Hr(),
    ]
)