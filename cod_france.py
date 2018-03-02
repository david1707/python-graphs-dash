import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('cod_france.csv')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Cause of Death in France',
            style={'textAlign': 'center'}),

    html.Div(children='Cause of Death in France between years 2001 and 2008 (included)',
            style={'textAlign': 'center'}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['TIME'] == i]['Value'],
                    y=df[df['TIME'] == i]['ICD10'],
                    text= "Deaths: " + df[df['TIME'] == i]['Value'] + ", Gender: " + df[df['TIME'] == i]['SEX'],
                    mode="markers",
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.TIME.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Value'},
                yaxis={'title': 'Cause of Death'},
                margin={'l': 200, 'b': 40, 't': 40, 'r': 40},

                hovermode='closest'
            )
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
