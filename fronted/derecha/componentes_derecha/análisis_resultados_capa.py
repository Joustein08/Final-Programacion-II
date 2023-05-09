from dash import html
import dash_bootstrap_components as dbc

analisis_resultados_capa = dbc.Container(
    [
        html.H2('ANÁLISIS DE RESULTADOS POR CAPA'),
        html.Hr(),
        dbc.Table(
            [
                html.Tr([
                    # Creacion celdas primera fila de la tabla
                    html.Td('CAPA', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                    html.Td('CATEGORIA 1', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                    html.Td('CATEGORIA 2', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                    html.Td('CATEGORIA 3', style={'background-color': 'black', 'fontWeight': 'bold', 'color': 'white', 'border': '1px solid white'}),
                ]),
                html.Tr([
                    # Creacion celdas segunda fila de la tabla
                    html.Td('CENTROS POBLADOS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFA0A0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFFFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#A0FFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                ]),
                html.Tr([
                    # Creacion celdas tercera fila de la tabla
                    html.Td('CARTOGRAFÍA', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFA0A0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFFFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#A0FFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                ]),
                html.Tr([
                    # Creacion celdas cuarta fila de la tabla
                    html.Td('CONSTRUCCIONES SIMILARES', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFA0A0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFFFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#A0FFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                ]),
                html.Tr([
                    # Creacion celdas quinta fila de la tabla
                    html.Td('FUENTES HÍDRICAS', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFA0A0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFFFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#A0FFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                ]),
                html.Tr([
                    # Creacion celdas sexta fila de la tabla
                    html.Td('VÍAS DE ACCESO', style={'background-color': 'white', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFA0A0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#FFFFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                    html.Td( style={'background-color': '#A0FFA0', 'fontWeight': 'bold', 'border': '1px solid black'}),
                ])
            ],
            style={'width': '100%'} #Hace que la tabla ocupe todo el ancho del container
        )        
    ]
)