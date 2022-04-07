import pandas as pd
import streamlit as st
import altair as alt
from dash import dcc
import plotly.graph_objs as go
import plotly.express as px
import protienShow
from annotated_text import annotated_text

file1 = open("alpha.txt","r")
data1=file1.read()

def variantDataShow(selected_variant):
    col1, col2, col3,col4, col5, col6 = st.columns([1,1,1,1,1,1])
    i=0
    col1, col2, col3,col4, col5, col6 = st.columns([1,1,1,1,1,1])
    with col1:
        st.button(label="Alpha",on_click=lambda variantName=i : variantDataShow("Alpha"))
    with col2:
        st.button(label="B.1.1.277",on_click=lambda variantName=i : variantDataShow("B.1.1.277"))
    with col3:
        st.button(label="B.1.1.302",on_click=lambda variantName=i : variantDataShow("B.1.1.302"))
    with col4:
        st.button(label="B.1.1.519",on_click=lambda variantName=i : variantDataShow("B.1.1.519"))

    with col5:
        st.button(label="B.1.160",on_click=lambda variantName=i : variantDataShow("B.1.160"))
    with col1:
        st.button(label="B.1.177",on_click=lambda variantName=i : variantDataShow("B.1.177"))
    with col2:
        st.button(label="B.1.221",on_click=lambda variantName=i : variantDataShow("B.1.221"))
    with col3:
        st.button(label="B.1.258",on_click=lambda variantName=i : variantDataShow("B.1.258"))
        
    with col4:
        st.button(label="B.1.367",on_click=lambda variantName=i : variantDataShow("B.1.367"))
    with col5:
        st.button(label="B.1.620",on_click=lambda variantName=i : variantDataShow("B.1.620"))
    with col1:
        st.button(label="Beta",on_click=lambda variantName=i : variantDataShow("Beta"))
    with col2:
        st.button(label="Delta",on_click=lambda variantName=i : variantDataShow("Delta"))

    with col3:
        st.button(label="Epsilon",on_click=lambda variantName=i : variantDataShow("Epsilon"))
    with col4:
        st.button(label="Eta",on_click=lambda variantName=i : variantDataShow("Eta"))
    with col5:
        st.button(label="Gamma",on_click=lambda variantName=i : variantDataShow("Gamma"))
    with col1:
        st.button(label="Iota",on_click=lambda variantName=i : variantDataShow("Iota"))
        
    with col2:
        st.button(label="Kappa",on_click=lambda variantName=i : variantDataShow("Kappa"))
    with col3:
        st.button(label="Lambda",on_click=lambda variantName=i : variantDataShow("Lambda"))
    with col4:
        st.button(label="Mu",on_click=lambda variantName=i : variantDataShow("Mu"))
    with col5:
        st.button(label="Omicron",on_click=lambda variantName=i : variantDataShow("Omicron"))
    
    with col1:
        st.button(label="S:677H.Robin1",on_click=lambda variantName=i : variantDataShow("S:677H.Robin1"))
    with col2:
        st.button(label="S:677P.Pelican",on_click=lambda variantName=i : variantDataShow("S:677P.Pelican"))
    with col3:
        st.button(label="others",on_click=lambda variantName=i : variantDataShow("others"))
    with col4:
        st.button(label="non_who",on_click=lambda variantName=i : variantDataShow("non_who"))
    st.write("### "+selected_variant+" Variant");
    path="Datasets/By Variant/"+selected_variant+"--CovidData.csv"
    demo_df = pd.read_csv(path)
    df = px.data.gapminder()
    fig = px.line(demo_df, x="date", y="perc_sequences",  line_group="variant", hover_name="perc_sequences",color='location', line_shape="spline", render_mode="svg")
    st.image("image1.png")
    st.plotly_chart(fig) 

    text_file = open("Datasets/protiens/"+selected_variant+".txt", "r")
    #read whole file to a string
    data = text_file.read()
    #close file
    protienShow.render_mol(data)
    annotated_text(data1)
