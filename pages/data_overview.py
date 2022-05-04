import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



def app():
    st.subheader('Data overview')
    chart_data = pd.DataFrame(
    np.random.rand(3, 4),
    index=["Train","Dev","Test"],)

    # Convert wide-form data to long-form
    # See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])

    # Horizontal stacked bar chart
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X("value", type="quantitative", title=""),
            y=alt.Y("index", type="nominal", title=""),
            color=alt.Color("variable", type="nominal", title="Classes"),
            order=alt.Order("variable", sort="descending"),
        )
        .properties(
    width=1000,
    height=200)
    )

    st.altair_chart(chart, use_container_width=True)