import dash
import pandas as pd
import numpy as np
from datetime import date

import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
            )

# Load Data
df = px.data.tips()

app.layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                html.H1(
                    children = "Personal Finance Visualistion",
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
                html.Div(
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                                    350, 430, 474, 526, 488, 537, 500, 439],
                                    name='Rest of world',
                                    marker=dict(
                                        color='rgb(55, 83, 109)'
                                    )
                                ),
                                dict(
                                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                                    299, 340, 403, 549, 499],
                                    name='China',
                                    marker=dict(
                                        color='rgb(26, 118, 255)'
                                    )
                                )
                            ],
                            layout=dict(
                                title='US Export of Plastic Scrap',
                                showlegend=True,
                                legend=dict(
                                    x=0,
                                    y=1.0
                                ),
                                margin=dict(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': '80vh'},
                        id='my-graph'
                    ),
                    style = {"margin": '0.5em'}
                ),
                width={"size": 12, "order": 2, },
                lg=8,
                align="center"  
                ),
            dbc.Col([

                html.H1(
                    children = "Enter the values for the asset",
                    className = "text-center mb-5"),

                html.H3(
                    children = "Principal Amount",
                    className = "text-center"),

                html.Div(
                    className = "d-flex flex-wrap justify-content-center p-1 center mb-4",
                    children = dcc.Input(
                        type="number", 
                        placeholder="Number",
                        min=500, max=500000000, step=500,
                    ),
                ),

                html.H3(
                    children = "Compounding Period",
                    className = "text-center"),

                dcc.Dropdown(
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
                    options=[
                        {'label': 'Yearly', 'value': 1},
                        {'label': 'Half-Yearly', 'value': 2},
                        {'label': 'Quarterly', 'value': 4},
                        {'label': 'Bi-Monthly', 'value': 6},
                        {'label': 'Monthly', 'value': 12},
                        {'label': 'Fortnightly', 'value': 26},
                        {'label': 'Weekly', 'value': 52},
                        {'label': 'Daily', 'value': 365},
                    ],
                    placeholder="Frequency",),
 
                html.H3(
                    children = "Date Range",
                    className = "text-center"),
                    
                dcc.DatePickerRange(
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
                    start_date_placeholder_text="Start Period",
                    end_date_placeholder_text="End Period",
                    start_date=date.today()),     

                html.H3(
                    children = "Annual Interest Rate",
                    className = "text-center"),

                dcc.Slider(
                    className = "d-flex justify-content-center p-1 m-1 mb-4",
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
                    value=6),
                   
                ],

                width={"size": 12, "order": 1},
                lg=4,
                align="center"
                ),
        ],
        justify="around",
        align="center"
    )
], fluid=True
)
# # Define callback to update graph
# @app.callback(
#     Output('graph', 'figure'),
#     [Input("colorscale-dropdown", "value")]
# )
# def update_figure(colorscale):
#     return px.scatter(
#         df, x="total_bill", y="tip", color="size",
#         color_continuous_scale=colorscale,
#         render_mode="webgl", title="Tips"
#     )


if __name__ == '__main__':
    app.run_server(debug=True)