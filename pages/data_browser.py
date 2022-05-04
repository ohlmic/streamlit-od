import streamlit as st
import pandas as pd
import os
from itertools import cycle

def app():
    st.subheader('Data browser')
    # filteredImages = os.listdir("images") # your images here
    # #caption = [] # your caption here
    # cols = cycle(st.columns(2)) # st.columns here since it is out of beta at the time I'm writing this
    # for idx, filteredImage in enumerate(filteredImages):
    #     next(cols).image(os.path.join('images', filteredImage), width=200) #, caption=caption[idx]
    
    image_files = os.listdir("images")
    image_index = st.slider('Choose an image', 1, len(image_files), 1)
    image = image_files[image_index - 1]
    st.image(os.path.join('images', image))

    

    
    