
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv("summary_data.csv")

# Split columns
left_columns = df.columns[df.index.get_loc("English DG"):df.index.get_loc("SPE average")+1]
right_columns = df.columns[df.index.get_loc("PreACT Composite Percentile PreACT"):]

# Create figure
fig = go.Figure()

# Left axis
for col in left_columns:
    mean = df.loc[col, 'Mean']
    lower = df.loc[col, 'Lower CI']
    upper = df.loc[col, 'Upper CI']
    fig.add_trace(go.Bar(name=col, x=[col], y=[mean], error_y=dict(type='data', array=[upper - mean], arrayminus=[mean - lower]), yaxis='y1'))

# Right axis
for col in right_columns:
    mean = df.loc[col, 'Mean']
    lower = df.loc[col, 'Lower CI']
    upper = df.loc[col, 'Upper CI']
    fig.add_trace(go.Bar(name=col, x=[col], y=[mean], error_y=dict(type='data', array=[upper - mean], arrayminus=[mean - lower]), yaxis='y2'))

# Layout
fig.update_layout(
    title="Percentile Distribution with Confidence Intervals",
    xaxis=dict(title="Metrics"),
    yaxis=dict(title="Scores (0-6)", range=[0, 6]),
    yaxis2=dict(title="Percentiles (0-100)", overlaying='y', side='right', range=[0, 100]),
    barmode='group'
)

# Display
st.title("Student Performance Dashboard")
st.plotly_chart(fig)
st.dataframe(df)
