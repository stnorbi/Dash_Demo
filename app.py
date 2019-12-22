import os
import dash
import dash_core_components as dcc
import dash_html_components as html

#own modules
from Modules import utils


app = dash.Dash(__name__)
server = app.server


app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])


#TODO: Itt add meg a CSS file-t!

@app.callback(dash.dependencies.Output('display-value', 'children'), [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)



if __name__ == '__main__':
    app.run_server(debug=True)

