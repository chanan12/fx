import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from datetime import datetime, timedelta

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label('History Duration:'),
    dcc.Input(id='input-text', type='text', value=''),
    html.Div(id='output-text')
])

@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_output(value):
    try:
        history_duration = int(value)
        current_date = datetime.now()
        start_date = current_date - timedelta(days=history_duration)
        return f'Start Date: {start_date}'
    except ValueError:
        return 'Please enter a valid integer for History Duration'

if __name__ == '__main__':
    app.run_server(debug=True)
