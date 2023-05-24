from dash import html
import dash_bootstrap_components as dbc


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
                html.Div(style={'width': f'{10}%', 'background-color': '#A0FFA0', 'height': '20px'}),
                html.Span(f'{10}%')
            ]),
        ]),
        html.Tr([
            html.Td('FUENTES HÍDRICAS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{30}%', 'background-color': '#A0FFA0', 'height': '20px'}),
                html.Span(f'{30}%')
            ]),
        ]),
        html.Tr([
            html.Td('CENTROS POBLADOS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{70}%', 'background-color': '#A0FFA0', 'height': '20px'}),
                html.Span(f'{70}%')
            ]),
        ]),
        html.Tr([
            html.Td('RED VIAL', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
            html.Td([
                html.Div(style={'width': f'{85}%', 'background-color': '#A0FFA0', 'height': '20px'}),
                html.Span(f'{85}%')
            ]),
        ]),       
    ],
    style={'width': '100%'}
        )        
    ]
    
)