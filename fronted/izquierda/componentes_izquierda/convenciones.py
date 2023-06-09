from dash import html
import dash_bootstrap_components as dbc

#Creacion container "CONVENCIONES"
convenciones = dbc.Container(
    [
        html.H2('CONVENCIONES'),
        html.Hr(),
        #Creacion tabla
        dbc.Table(
            [
                html.Tr([
                    # Creacion celdas primera fila de la tabla
                    html.Td('MALO', style={'background-color': 'red', 'fontWeight': 'bold'}),
                    html.Td('REGULAR', style={'background-color': 'yellow', 'fontWeight': 'bold'}),
                    html.Td('BUENO', style={'background-color': 'green', 'fontWeight': 'bold'}),
                ]),
            ],
            style={'width': '100%'} #Hace que la tabla ocupe todo el ancho del container
        )
    ]
)