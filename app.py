import streamlit as st
from multiapp import MultiApp
from apps import home, variants # import your app modules here


app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Variants", variants.app)
# app.add_app("Model", model.app)
# The main app
app.run()