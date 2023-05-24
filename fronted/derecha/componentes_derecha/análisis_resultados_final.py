from dash import html, dcc
import dash_bootstrap_components as dbc

analisis_resultados_final = dbc.Container(
     [         
         html.H2('ANÁLISIS DE RESULTADOS FINAL'),
         html.Hr(),
         html.H5('Según el análisis generado por el software se especifica:'),
         html.Hr(),
         html.Br(),
         dbc.Button("Mostrar Salidas", id="boton-mostrar-salidas", color="dark", className=""),
         html.Div(id="salidas"),
        #  html.Label('Análisis de construcciones similares'),
        #  html.Hr(),
        #  html.Div(id = 'salidaConstrucciones'),
        #  html.Hr(),
        #  html.Label('Análisis de cuerpos de agua'),
        #  html.Hr(),
        #  html.Div(id = 'salidaRios'),
        #  html.Label('Análisis de cercanía de población'),
        #  html.Hr(),
        #  html.Div(id = 'salidaPoblacion'),
         # html.Label('Análisis de a cuerdo a la red vial'),
         # html.Hr(),
         # html.Div(id = 'salidaVias'),
     ]
 )