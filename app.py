import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load summary data
summary_df = pd.read_csv("summary_data.csv")

st.title("DASH Student Performance Evaluation (2025-2026)")

st.subheader("Percentile Distribution Graph with Confidence Intervals")

fig = go.Figure()

# Add score columns (Y-axis 1)
for _, row in summary_df[summary_df["Type"] == "Score"].iterrows():
    fig.add_trace(go.Bar(
        x=[row["Metric"]],
        y=[row["Mean"]],
        name=row["Metric"],
        error_y=dict(type='data', symmetric=False, array=[row["CI Upper"] - row["Mean"]], arrayminus=[row["Mean"] - row["CI Lower"]]),
        marker_color='blue',
        yaxis='y1'
    ))

# Add percentile columns (Y-axis 2)
for _, row in summary_df[summary_df["Type"] == "Percentile"].iterrows():
    fig.add_trace(go.Bar(
        x=[row["Metric"]],
        y=[row["Mean"]],
        name=row["Metric"],
        error_y=dict(type='data', symmetric=False, array=[row["CI Upper"] - row["Mean"]], arrayminus=[row["Mean"] - row["CI Lower"]]),
        marker_color='orange',
        yaxis='y2'
    ))

fig.update_layout(
    barmode='group',
    xaxis=dict(title='Metrics'),
    yaxis=dict(title='Scores (0-6)', range=[0, 6]),
    yaxis2=dict(title='Percentiles (0-100)', overlaying='y', side='right', range=[0, 100]),
    legend=dict(x=1.05, y=1),
    margin=dict(l=40, r=40, t=40, b=40),
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Summary Table with Confidence Intervals")
st.dataframe(summary_df)
