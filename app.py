import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load cleaned data
df = pd.read_csv("formatted_sales_data.csv")

df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

df = df.groupby("Date", as_index=False)["Sales"].sum()
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsels Sales Over Time",
    labels={"Date": "Date", "Sales": "Total Sales"}
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# NEW way to run server
if __name__ == "__main__":
    app.run(debug=True)
