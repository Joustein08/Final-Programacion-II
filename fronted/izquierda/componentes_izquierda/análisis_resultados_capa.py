from dash import html
import dash_bootstrap_components as dbc
from Backend.Final import porcentaje_influencia1
from Backend.Final import porcentaje_influencia2
from Backend.Final import porcentaje_influencia3
from Backend.Final import porcentaje_influencia4

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
        dbc.Table(
            [
        html.Tr([
            html.Td('CAPA',style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
            html.Td('FACTIBILIDAD',style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
        ]),
        html.Tr([
            html.Td('CONSTRUCCIONES SIMILARES', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{round(porcentaje_influencia2, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia2), 'height': '20px'}),
                html.Span(f'{round(porcentaje_influencia2, 2)}%')
            ]),
        ]),
        html.Tr([
            html.Td('FUENTES HÍDRICAS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{round(porcentaje_influencia4, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia4), 'height': '20px'}),
                html.Span(f'{round(porcentaje_influencia4, 2)}%')
            ]),
        ]),
        html.Tr([
            html.Td('CENTROS POBLADOS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{round(porcentaje_influencia3, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia3), 'height': '20px'}),
                html.Span(f'{round(porcentaje_influencia3, 2)}%')
            ]),
        ]),
        html.Tr([
            html.Td('RED VIAL', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{round(porcentaje_influencia1, 2)}%', 'background-color': asignar_color_porcentaje(porcentaje_influencia1), 'height': '20px'}),
                html.Span(f'{round(porcentaje_influencia1, 2)}%')
            ]),
        ]),       
    ],
    style={'width': '100%'}
        )        
    ]
    
)