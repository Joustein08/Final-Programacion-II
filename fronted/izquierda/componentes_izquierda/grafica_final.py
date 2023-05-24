from dash import html
import dash_bootstrap_components as dbc

grafica_final = dbc.Container(
    [
        html.H2('GRÁFICA FINAL'),
        html.Br(),
        dbc.Button("Mostrar Análisis Final", id="boton-mostrar-final", color="primary", className="mr-2"),
        html.Div(id="salidaGraficaFinal"),
    ]
)