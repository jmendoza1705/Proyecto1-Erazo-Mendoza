import dash
from dash import dcc  # dash core components
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {'background': '#E6CDFA','color': '#521383'}

app.layout = html.Div(children=[

    html.H1('Sistema de Predicción de Enfermedad Cardíaca', style={'backgroundColor': colors['background'],
                                                                   'textAlign': 'center'}),

    html.Div(html.H6('Este sistema permite realizar predicciones del riesgo de sufrir una enfermedad cardíaca para determinar '
             'el proceso adecuado a seguir, en busca del bienestar del paciente. Para esto, se tienen en cuenta los '
             'siguientes parámetros:')),

    html.Div(html.H6(dcc.Markdown('''
    * **Edad (Age):** Edad del paciente (años).
    * **Glucosa (FBS):** Nivel de glucosa en sangre en ayunas mayor a 120 mg/dl.
    * **Colesterol (CHOL):** Valor de colesterol total en sangre (mg/dl).
    * **ST (OLDPEAK):** Depresión del ST inducida por el ejercicio en relación con el reposo.
    * **Angina (EXANG):** Angina inducida por el ejercicio. 
    * **Talasemia (THAL):** Tipo de talasemia.
    '''))),

    html.Div(html.H4('Seleccione los valores de los parámetros'), style={'backgroundColor': colors['background'],
                                                                   'textAlign': 'center'}),


    # Parametros:
    html.Div([
    html.Div(html.H6("Edad (Age)", style={"color": "#521383"})),
    html.Div('''30: 29 a 39 años / 40: 40 a 49 años / 50: 50 a 59 años / 60: 60 a 69 años / 70: Mayor de 70 años'''),
    html.Div([
        dcc.Dropdown(
            id='Edad',
            options=[{'label': i, 'value': i} for i in [30, 40, 50, 60, 70]])], style={'width': '35%'}),


    html.Div(html.H6("Glucosa (FBS)", style={"color": "#521383"})),
    html.Div("0: No / 1: Sí"),
    html.Div([
        dcc.Dropdown(
            id='Glucosa',
            options=[{'label': i, 'value': i} for i in [0, 1]])], style={'width': '35%'})], style= {'columnCount': 2}),

    html.Div([
    html.Div(html.H6("Colesterol (CHOL)", style={"color": "#521383"})),
    html.Div("0: menos de 200 / 1: Entre 200 y 239 / 2: Mayor o igual a 240"),
    html.Div([
        dcc.Dropdown(
            id='Colesterol',
            options=[{'label': i, 'value': i} for i in [0, 1, 2]])], style={'width': '35%'}),


    html.Div(html.H6("ST (OLDPEAK)", style={"color": "#521383"})),
    html.Div("0: Menos de 2 / 1: Entre 2 y 4 / 2: Mayor o igual a 4"),
    html.Div([
        dcc.Dropdown(
            id='ST',
            options=[{'label': i, 'value': i} for i in [0, 1, 2]])], style={'width': '35%'})], style= {'columnCount': 2}),

    html.Div([
    html.Div(html.H6("Angina (EXANG)", style={"color": "#521383"})),
    html.Div("1: Sí / 2: No"),
    html.Div([
        dcc.Dropdown(
            id='EXANG',
            options=[{'label': i, 'value': i} for i in [1, 2]])], style={'width': '35%'}),

    html.Div(html.H6("Talasemia (THAL)", style={"color": "#521383"})),
    html.Div("3: Normal / 6: Defecto fijo / 7: Defecto reversible"),
    html.Div([
        dcc.Dropdown(
            id='Talasemia',
            options=[{'label': i, 'value': i} for i in [3, 6, 7]])], style={'width': '35%'})], style= {'columnCount': 2}),


    html.Div([
        html.Br(),
        html.Br(),
        html.Button('Realizar predicción', id='button'),
        dcc.Interval(id='interval', interval=500)]),

    dcc.Graph(id='graph-prob')

])

@app.callback(
    Output('graph-prob', "figure"),
    [Input('Edad', 'value'),
     Input('Glucosa', 'value'),
     Input('Colesterol', 'value'),
     Input('ST', 'value'),
     Input('EXANG', 'value'),
     Input('Talasemia', 'value')])

def update_output_div(Edad, Glucosa, Colesterol, ST, EXANG, Talasemia):
    fig = px.bar(Edad)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, port=9877)

   ##
@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


