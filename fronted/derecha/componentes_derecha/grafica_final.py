from dash import html
import dash_bootstrap_components as dbc

grafica_final = dbc.Container(
    [
        html.H2('GRÁFICA FINAL'),
        html.Hr(),
        html.Img(src='C:/Users/usuario/Desktop/Proyecto programación II/Imagenes/Ubicacion.png', style={'width': '50%'}),
        html.Br(),
        dbc.Button('Descargar', color='primary', className='mr-2'),
        html.Hr(),
    ]
)