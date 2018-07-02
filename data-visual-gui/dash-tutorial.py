import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash tutorials'),
    dcc.Graph(id='example',
            figure={
                'data': [
                    {'x':[1,2,3,4,5], 'y':[12,4,15,18,7], 'type':'line', 'name':'boats'},
                    {'x':[1,2,3,4,5], 'y':[5,17,4,12,15], 'type':'bar', 'name':'cars'},
                    ],
                'layout': {
                    'title':'Basic Dash Example'
                }
            })
    ])


if __name__=='__main__':
    app.run_server(debug=True)