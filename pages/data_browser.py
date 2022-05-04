import streamlit as st
import pandas as pd
import os
from itertools import cycle

def app():
    st.subheader('Data browser')
    filteredImages = os.listdir("images") # your images here
    #caption = [] # your caption here
    cols = cycle(st.columns(2)) # st.columns here since it is out of beta at the time I'm writing this
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(os.path.join('images', filteredImage), width=200) #, caption=caption[idx]

    
    