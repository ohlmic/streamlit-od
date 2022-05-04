import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import data_browser, machine_learning, data_overview #, metadata, data_visualize, redundant, inference # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Object Detection App")

# Add all your applications (pages) here
app.add_page("Data Browser", data_browser.app)
app.add_page("Data Overview", data_overview.app)
app.add_page("Machine Learning", machine_learning.app)
#app.add_page("Data Analysis",data_visualize.app)
#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()