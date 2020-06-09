import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from flask import Flask
df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'
app.layout = html.Div([dcc.Graph(figure=fig)])
if __name__ == '__main__':
    app.run_server()
