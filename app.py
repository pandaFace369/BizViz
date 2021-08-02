import dash
import pandas as pd
import numpy as np
from datetime import date

import plotly.express as px
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.io as pio
pio.templates

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
            )

# Load Data
df = pd.DataFrame.from_records([{'Principal': 0, 'Rate': 0, 'Frequency': 0, 'StartDate': 0, 'EndDate': 0}])
    
df2 = px.data.gapminder()
df_2007 = df2.query("year==2007")

fig = px.scatter(df_2007,
                     x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True,
                     template='plotly_dark', title="Gapminder 2007")

app.layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                html.H1(
                    children = "Personal Finance Visualistion",
                    className = "font-weight-bolder",
                    style = {
                        'textAlign': 'center',
                        'padding': '0.5em',
                        'color': 'white'
                    }
                ), 
                width = 12
            )
        ],
        align="center",
    ),
    dbc.Row(
        [
            dbc.Col([
                
                html.H2(
                    children = "Finance Plot",
                    className = "font-weight-bolder",
                    style = {
                        'textAlign': 'center',
                        'padding': '0.5em',
                        'color': 'white'
                    }
                ), 

                html.Div(
                    dcc.Graph(figure=fig),
                    style = {"margin": '0.5em'}
                ),
           ],
                width={"size": 12, "order": 2, },
                lg=8,
                align="center"
            ),


            dbc.Col([

                html.H2(
                    children = "Finance Calculator",
                    className = "font-weight-bolder",
                    style = {
                        'textAlign': 'center',
                        'padding': '0.5em',
                        'color': 'white'
                    }
                ), 

                html.H3(
                    children = "Principal Amount",
                    className = "text-center"
                ),

                html.Div(
                    className = "d-flex flex-wrap justify-content-center p-3 center mb-4",
                    children = dcc.Input(
                        id = "Principal",
                        type="number",
                        value= 500,
                        placeholder="Number",
                        min=500, max=500000000, step=500,
                        className = "d-flex flex-wrap text-center p-3",
                    ),
                ),

                html.H3(
                    children = "Compounding Period",
                    className = "text-center"
                ),

                dcc.Dropdown(
                    id="Frequency",
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
                    value = 0,
                    options=[
                        {'label': 'One-time', 'value': 0},
                        {'label': 'Yearly', 'value': 1},
                        {'label': 'Half-Yearly', 'value': 2},
                        {'label': 'Quarterly', 'value': 4},
                        {'label': 'Bi-Monthly', 'value': 6},
                        {'label': 'Monthly', 'value': 12},
                        {'label': 'Fortnightly', 'value': 26},
                        {'label': 'Weekly', 'value': 52},
                        {'label': 'Daily', 'value': 365},
                    ],
                    placeholder="Frequency",
                ),
 
                html.H3(
                    children = "Date Range",
                    className = "text-center"
                ),
                    
                dcc.DatePickerRange(
                    id = "DateRange",
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
                    start_date_placeholder_text="Start Period",
                    display_format='DD/ MM/ YYYY',
                    end_date_placeholder_text="End Period",
                    start_date=date.today(),
                    end_date=date.today()
                ),     

                html.H3(
                    children = "Annual Interest Rate",
                    className = "text-center"
                ),

                dcc.Slider(
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
                    id = "Rate",
                    min=0,
                    max=25,
                    step=0.01,
                    marks={
                        0: '0 %',
                        3: '3 %',
                        6: '6 %',
                        12: '12%',
                        25: '25%'
                    },
                    value=6
                ),

                html.Div([

                    html.Div([
                            html.Button("Save", id="save-data", className = "btn btn-outline-secondary m-2 p-2 pl-5 pr-5", n_clicks=0)
                    ]),

                    html.Div([
                            html.Button("Download", id="download-data", className = "btn btn-outline-secondary m-2 p-2 pl-5 pr-5", n_clicks=0),
                            dcc.Download(id="download-dataframe-xlsx"),
                        ],
                    ),
                    
                    html.Div([
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div([
                                'Upload'
                            ]),
                            className = "btn btn-outline-secondary m-2 p-2 pl-5 pr-5"
                        )
                    ])
                ],
                className = "d-flex flex-row justify-content-around pt-4"
                )     
            ],
            width={"size": 12, "order": 1},
            lg=4,
            align="center"
            ),
        ],
        justify="around",
        align="center"
    ),
    dbc.Row(
        [
            dbc.Col(
                html.H2(
                    children = "Finance Dataset",
                    className = "font-weight-bolder",
                    style = {
                        'textAlign': 'center',
                        'padding': '0.5em',
                        'color': 'white'
                    }
                ), 
                width = 12
            )
        ],
        align="center",
    ),
    dbc.Row(
        [
            dbc.Col(
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    page_size=10,
                    editable=True,                  # allow user to edit data inside tabel
                    row_deletable=True,             # allow user to delete rows
                    sort_action="native",           # give user capability to sort columns
                    sort_mode="single",             # sort across 'multi' or 'single' columns
                    filter_action="native",         # allow filtering of columns
                    style_header={'backgroundColor':'#37536D'},
                    style_cell={
                        'backgroundColor': '#002B36',
                    },
                )
            )
        ],
        align="center",
    ),
], fluid=True
)

@app.callback(
    Output('table', 'data'),
    [Input('save-data', 'n_clicks'), 
    Input('Principal', 'value'), 
    Input('Rate', 'value'), 
    Input('Frequency', 'value'),
    Input('DateRange', 'start_date'),
    Input('DateRange', 'end_date')]
)
def add_row(n_clicks, principal, rate, frequency, startDate, endDate):
    row = {'Principal': principal, 'Rate': rate, 'Frequency': frequency, 'Start Date': startDate, 'End Date': endDate}
    if n_clicks > 0:  
        df.append(row, ignore_index=True)
        print(df)

if __name__ == '__main__':
    app.run_server(debug=True)