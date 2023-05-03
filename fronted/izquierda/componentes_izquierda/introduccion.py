from dash import html
import dash_bootstrap_components as dbc

introduccion = dbc.Container(
    [
        html.H2('INTRODUCCIÓN'),
        html.Hr(),
        html.H6('Ésta aplicación colaborativa puede ser útil para la planificación de sus proyectos de infraestructura. La información que proporcione le permitirá visualizar de manera gráfica la zona idónea para su ubicación, según las zonas de riesgo  presentes en el área de influencia de su proyecto, con cobertura en todo el territorio nacional.', style={'text-justify': 'inter-word'}),
        html.Hr(),
    ]
)
