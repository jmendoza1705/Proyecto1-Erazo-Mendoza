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
    * **Edad:** Edad del paciente (años).
    * **Glucosa:** Nivel de glucosa en sangre en ayunas mayor a 120 mg/dl.
    * **Colesterol:** Valor de colesterol total en sangre (mg/dl).
    * **CP:** Tipo de dolor en el pecho.
    * **ST:** Depresión del ST inducida por el ejercicio en relación con el reposo.
    * **EXANG:** Angina inducida por el ejercicio. 
    * **Talasemia:** Tipo de talasemia.
    '''))),

    html.Div(html.H4('Seleccione los valores de los parámetros'), style={'backgroundColor': colors['background'],
                                                                   'textAlign': 'center'}),


    # Parametros:
    html.Div(html.H6("Edad", style={"color": "#521383"})),
    html.Div('''30: 29 a 39 años / 40: 40 a 49 años / 50: 50 a 59 años / 60: 60 a 69 años / 70: Mayor de 70 años'''),
    html.Div([
        dcc.Dropdown(
            id='Edad',
            options=[{'label': i, 'value': i} for i in [30, 40, 50, 60, 70]],
            value='Edad')],style={'width': '35%', 'display': 'inline-block'}),


    html.Div(html.H6("Glucosa", style={"color": "#521383"})),
    html.Div("0: No / 1: Sí"),
    html.Div([
        dcc.Dropdown(
            id='Glucosa',
            options=[{'label': i, 'value': i} for i in [0, 1]],
            value='Glucosa')], style={'width': '35%', 'display': 'inline-block'}),

    html.Div(html.H6("Colesterol", style={"color": "#521383"})),
    html.Div("0: menos de 200 / 1: Entre 200 y 239 / 2: Mayor o igual a 240"),
    html.Div([
        dcc.Dropdown(
            id='Colesterol',
            options=[{'label': i, 'value': i} for i in [0, 1, 2]],
            value='Colesterol')], style={'width': '35%', 'display': 'inline-block'}),

    html.Div(html.H6("CP", style={"color": "#521383"})),
    html.Div("1: Angina Típica / 2: Angina Atípica / 3: Dolor no Anginoso / 4: Asintomático"),
    html.Div([
        dcc.Dropdown(
            id='CP',
            options=[{'label': i, 'value': i} for i in [1, 2, 3, 4]],
            value='CP')], style={'width': '35%', 'display': 'inline-block'}),

    html.Div(html.H6("ST", style={"color": "#521383"})),
    html.Div("0: Menos de 2 / 1: Entre 2 y 4 / 2: Mayor o igual a 4"),
    html.Div([
        dcc.Dropdown(
            id='ST',
            options=[{'label': i, 'value': i} for i in [0, 1, 2]],
            value='ST')], style={'width': '35%', 'display': 'inline-block'}),

    html.Div(html.H6("EXANG", style={"color": "#521383"})),
    html.Div("1: Sí / 2: No"),
    html.Div([
        dcc.Dropdown(
            id='EXANG',
            options=[{'label': i, 'value': i} for i in [1, 2]],
            value='EXANG')], style={'width': '35%', 'display': 'inline-block'}),

    html.Div(html.H6("Talasemia", style={"color": "#521383"})),
    html.Div("3: Normal / 6: Defecto fijo / 7: Defecto reversible"),
    html.Div([
        dcc.Dropdown(
            id='Talasemia',
            options=[{'label': i, 'value': i} for i in [3, 6, 7]],
            value='Talasemia')], style={'width': '35%', 'display': 'inline-block'}),

])


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, port=9877)

