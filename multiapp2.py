import streamlit as st

class MultiApp2:
    def __init__(self):
        self.apps2 = []

    def add_app2(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps2.append({
            "title": title,
            "function": func
        })  

    def run2(self):
        app = st.sidebar.selectbox(
            'Variant Navigation',
            self.apps2,
            format_func=lambda app: app['title'])
        app['function']()