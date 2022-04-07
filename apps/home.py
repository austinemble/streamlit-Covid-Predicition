import streamlit as st
import pandas as pd
def app():
    st.header("Covid Predicition")
    st.write("""
        ### What is Covid-19?
        COVID-19 (coronavirus disease 2019) is a disease caused by a virus named SARS-CoV-2 and was discovered in December 2019 in Wuhan, China. It is very contagious and has quickly spread around the world. 
        COVID-19 most often causes respiratory symptoms that can feel much like a cold, a flu, or pneumonia. COVID-19 may attack more than your lungs and respiratory system. Other parts of your body may also be affected by the disease.
        * Most people with COVID-19 have mild symptoms, but some people become severely ill.
        * Some people including those with minor or no symptoms may suffer from post-COVID conditions — or “long COVID”.
        * Older adults and people who have certain underlying medical conditions are at increased risk of severe illness from COVID-19.
        * Hundreds of thousands of people have died from COVID-19 in the United States.
        * Vaccines against COVID-19 are safe and effective. Vaccines teach our immune system to fight the virus that causes COVID-19.
    """)
    df = pd.read_csv("Datasets/covid-variants.csv")
    variantAll = df.variant.unique()
    variantAll