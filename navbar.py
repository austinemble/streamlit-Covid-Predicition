import streamlit as st
import pandas as pd
import variantsApps.variantTemplate as variantTemplate;
def navBar():  
  # Nav Bar Section
  st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
    <a class="navbar-brand" href="/" target="_blank">Covid Variant Prediction</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="" target="_blank">Mutations</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="" target="_blank">Per Variant</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="" target="_blank">Per Country</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="" target="_blank">Acknowledgements</a>
        </li>
      </ul>
    </div>
  </nav>
  """, unsafe_allow_html=True)

  st.markdown('''# **Covid Variant Prediction**
  ''')


  st.markdown("""
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  """, unsafe_allow_html=True)

  # Side Bar section
  df =pd.read_csv("Datasets/covid-variants.csv")
  countrysList = df.location.unique();
  variantsList = df.variant.unique();
  st.sidebar.header(' Variant')
  for i in variantsList:
    variantName= i
    st.sidebar.button(label=variantName,on_click=lambda variantName=i : variantTemplate.variantDataShow(variantName))