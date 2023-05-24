from dash import html
import dash_bootstrap_components as dbc

grafica_final = dbc.Container(
    [
        html.H2('GRÁFICA FINAL'),
        html.Br(),
        dbc.Button("Mostrar Análisis final", id="boton-mostrar-salidas", color="dark", className=""),
        html.Div(id="salidaGraficaFinal"),
    ]
)