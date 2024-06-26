import dash_bootstrap_components as dbc
import pandas as pd
import datetime
from dash import html, dcc
from src.data import df

current_date = datetime.datetime.now().strftime("%B %d, %Y")

heatmap_salary_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Global Heatmap of Average Salaries by Country"),
            dcc.Loading(
                type="default",
                children=dcc.Graph(id="heatmap_salary")
            )
        ]
    )
)

histogram_salary_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Salary Distribution"),
            dcc.Loading(
                type="default",
                children=dcc.Graph(id="histogram_salary")
            )
        ]
    )
)

box_plot_by_experience_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Box Plot by Experience"),
            dcc.Loading(
                type="default",
                children=dcc.Graph(id="box_plot_by_experience")
            )
        ]
    ),
    className="h-100"
)

box_plot_by_work_arrangement_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Box Plot by Work Arrangement"),
            dcc.Loading(
                type="default",
                children=dcc.Graph(id="box_plot_by_work_arrangement")
            )
        ]
    ),
    className="h-100"
)

bar_chart_top_jobs_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Bar Chart For Job Average Salary Rankings"),
            dcc.Loading(
                type="default",
                children=dcc.Graph(id="bar_chart_top_jobs")
            ),
            html.Label("Job Average Salary Rankings Range:", style={'font-weight': 'bold', 'text-align': 'left'}),
            dcc.RangeSlider(
                id='job_title_range_slider',
                min=0, 
                max=10,  # Example range for job title slider
                value=[0, 10],
                step=1, 
                marks= None,  # Example marks
                tooltip={"placement": "bottom", "always_visible": True}
            ),
        ],
        style={'display': 'flex', 'flex-direction': 'column', 'flex': '1'}
    ),
    className="h-100"
)

layout = dbc.Container(
    [
        html.H1("DS Compensations Insights",style={'background-color': '#636EFA', 'color': 'white', 'padding': '10px'}),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dbc.Row([
                    dbc.Col(dbc.Label("Continents", style={'font-weight': 'bold', 'text-align': 'right'})),
                    dbc.Col(dcc.Dropdown(
                        id="filter-continent",
                        options=[{"label": level, "value": level} for level in df['continent'].unique()],
                        value=[level for level in df['continent'].unique()],
                        multi=True,
                        placeholder="Select Continent(s)",
                    ), width=11)
                ], align="left"),
                width=12
            )
        ]),
        
        html.Hr(style={'borderTop': '1px solid #ccc', 'marginBottom': '10px'}),
        dbc.Row([
            dbc.Col(heatmap_salary_card, md=8),
            dbc.Col(histogram_salary_card, md=4),
        ]),
        html.Hr(style={'borderTop': '1px solid #ccc', 'marginBottom': '10px'}),
        dbc.Row([
            dbc.Col(box_plot_by_experience_card, md=4),
            dbc.Col(box_plot_by_work_arrangement_card, md=4),
            dbc.Col(bar_chart_top_jobs_card, md=4),
        ], align="stretch"),
        html.Footer([
            html.Hr(style={'borderTop': '1px solid #ccc', 'marginBottom': '10px'}),
            html.P("This app provides data-driven insights into data science compensation. Created by Dan Zhang, Doris Cai, Jordan Cairns, Sho Inagaki.", 
                style={'fontSize': '12px', 'margin': '0', 'padding': '2px 0'}),
            html.A("GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2024_7_ds-compensation", target="_blank", 
                style={'fontSize': '10px', 'display': 'block', 'margin': '0', 'padding': '2px 0'}),
            html.P(f"Last updated: {current_date}", 
                style={'fontSize': '8px', 'margin': '0', 'padding': '2px 0'})
        ], style={'textAlign': 'center', 'marginTop': '20px', 'paddingTop': '10px', 'paddingBottom': '10px'})
    ],
    fluid=True,
)
