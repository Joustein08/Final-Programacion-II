from dash import html
import dash_bootstrap_components as dbc

def asignar_color_porcentaje(porcentaje):
    if porcentaje <= 30:
        return '#FF0000'  # Rojo
    elif porcentaje <= 50:
        return '#FFFF00'  # Amarillo
    else:
        return '#00FF00'  # Verde


analisis_resultados_capa = dbc.Container(
    [
        html.H2('ANÁLISIS DE RESULTADOS POR CAPA'),
        html.Hr(),
        dbc.Button('Generar tabla', id='boton-generar-tabla',color="dark", className=""),
        html.Hr(),
        html.Div(id='tabla-container')
    ]
)