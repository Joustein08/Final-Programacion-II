from dash import html
import dash_bootstrap_components as dbc

analisis_resultados_final = dbc.Container(
     [         
         html.H2('ANÁLISIS DE RESULTADOS FINAL'),
         html.Hr(),
         html.H5('Según el análisis generado por el software se especifica:'),
         html.Hr(),
         html.Br(),
         dbc.Button("Mostrar Salidas", id="boton-mostrar-salidas", color="primary", className="mr-2"),
         html.Div(id="salidas"),
     ]
 )