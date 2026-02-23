import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create Dash app
app = dash.Dash(__name__)

# Layout with styling
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "40px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Soul Foods Pink Morsels Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div(
            style={"textAlign": "center", "marginBottom": "30px"},
            children=[
                html.Label("Select Region:",
                           style={"fontSize": "20px", "marginRight": "20px"}),

                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                ),
            ]
        ),

        dcc.Graph(id="sales-chart")
    ]
)

# Callback for updating chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    grouped = filtered_df.groupby("Date", as_index=False)["Sales"].sum()
    grouped = grouped.sort_values("Date")

    fig = px.line(
        grouped,
        x="Date",
        y="Sales",
        title="Pink Morsels Sales Over Time",
        labels={"Date": "Date", "Sales": "Total Sales"}
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f9"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
