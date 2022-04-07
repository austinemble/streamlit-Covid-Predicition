import pandas as pd
import streamlit as st
import altair as alt
from dash import dcc
import plotly.graph_objs as go
import plotly.express as px

def variantDataShow(selected_variant):
    st.write("### "+selected_variant+" Variant");
    path="Datasets/By Variant/"+selected_variant+"--CovidData.csv"
    demo_df = pd.read_csv(path)
    # jsonData = pd.read_json("data.json");
    # st.markdown(jsonData)
    df = px.data.gapminder()
    fig = px.line(demo_df, x="date", y="perc_sequences",  line_group="variant", hover_name="perc_sequences",color='location', line_shape="spline", render_mode="svg")
    st.plotly_chart(fig) 