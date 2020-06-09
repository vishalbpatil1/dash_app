import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
url="https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df=pd.read_csv(url)
fig = px.scatter(df, x="sepal_width", y="sepal_length")
#fig.show()
app = dash.Dash(__name__)
app.layout = html.Div([dcc.Graph(figure=fig)])
if __name__ == '__main__':
    app.run_server()
