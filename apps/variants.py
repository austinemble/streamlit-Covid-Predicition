
from matplotlib import container
import streamlit as st
import numpy as np
import pandas as pd
from annotated_text import annotated_text
import variantTemplate



def app():
    st.title('Overview of Variants/Mutations')
    st.write("""
    Click one of the colored buttons to look at a particular Variant - to read information, see graphs and the protein structure, and link out to focused Nextstrain builds.

To look at many variants at once, check out the Per Variant and Per Country pages, where you can view a lot of data in the same place, and compare variants and countries!

Variants included on CoVariants include internationally recognised Variants of Concern (VoC) and many Variants of Interest (VoI), as well as other variants which have expanded rapidly, dominated in countries or regions, or feature mutations of interest.

Mutations included on CoVariants are mutations associated with VoCs or other variants, which have an association with observed or hypothetical changes in viral transmission, immune escape, or clinical outcome.
    """)

    df =pd.read_csv("Datasets/covid-variants.csv")
    countrysList = df.location.unique();
    variantsList = df.variant.unique();
    st.sidebar.header(' Variant')
    col1, col2, col3,col4, col5, col6 = st.columns([1,1,1,1,1,1])

    i=0
    
    with col1:
        st.button(label="Alpha",on_click=lambda variantName=i : variantTemplate.variantDataShow("Alpha"))
    with col2:
        st.button(label="B.1.1.277",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.1.277"))
    with col3:
        st.button(label="B.1.1.302",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.1.302"))
    with col4:
        st.button(label="B.1.1.519",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.1.519"))

    with col1:
        st.button(label="B.1.160",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.160"))
    with col2:
        st.button(label="B.1.177",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.177"))
    with col3:
        st.button(label="B.1.221",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.221"))
    with col4:
        st.button(label="B.1.258",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.258"))
        
    with col1:
        st.button(label="B.1.367",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.367"))
    with col2:
        st.button(label="B.1.620",on_click=lambda variantName=i : variantTemplate.variantDataShow("B.1.620"))
    with col3:
        st.button(label="Beta",on_click=lambda variantName=i : variantTemplate.variantDataShow("Beta"))
    with col4:
        st.button(label="Delta",on_click=lambda variantName=i : variantTemplate.variantDataShow("Delta"))

    with col1:
        st.button(label="Epsilon",on_click=lambda variantName=i : variantTemplate.variantDataShow("Epsilon"))
    with col2:
        st.button(label="Eta",on_click=lambda variantName=i : variantTemplate.variantDataShow("Eta"))
    with col3:
        st.button(label="Gamma",on_click=lambda variantName=i : variantTemplate.variantDataShow("Gamma"))
    with col4:
        st.button(label="Iota",on_click=lambda variantName=i : variantTemplate.variantDataShow("Iota"))
        
    with col1:
        st.button(label="Kappa",on_click=lambda variantName=i : variantTemplate.variantDataShow("Kappa"))
    with col2:
        st.button(label="Lambda",on_click=lambda variantName=i : variantTemplate.variantDataShow("Lambda"))
    with col3:
        st.button(label="Mu",on_click=lambda variantName=i : variantTemplate.variantDataShow("Mu"))
    with col4:
        st.button(label="Omicron",on_click=lambda variantName=i : variantTemplate.variantDataShow("Omicron"))
    
    with col1:
        st.button(label="S:677H.Robin1",on_click=lambda variantName=i : variantTemplate.variantDataShow("S:677H.Robin1"))
    with col2:
        st.button(label="S:677P.Pelican",on_click=lambda variantName=i : variantTemplate.variantDataShow("S:677P.Pelican"))
    with col3:
        st.button(label="others",on_click=lambda variantName=i : variantTemplate.variantDataShow("others"))
    with col4:
        st.button(label="non_who",on_click=lambda variantName=i : variantTemplate.variantDataShow("non_who"))
            