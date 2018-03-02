import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_clean.csv')


app.layout = html.Div([

    html.H1(
        children="Titanic travelers by Age/Home destination",
        style={'textAlign': 'center'}),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['sex'] == i]['age'],
                    y=df[df['sex'] == i]['home.dest'],
                    text="Name: " + df[df['sex'] == i]['name'] + ", Ticket: " + df[df['sex'] == i]['ticket'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.sex.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Age'},
                yaxis={'title': 'Home Destination'},
                margin={'l': 200, 'b': 40, 't': 40, 'r': 40},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
