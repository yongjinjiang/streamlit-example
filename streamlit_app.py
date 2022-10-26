from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st

midx = pd.MultiIndex.from_product([['ix', 'jy'], [0, 1], ['x3', 'z4']])
df = pd.DataFrame([np.arange(8)], columns=midx)
def highlight_x(s):
    return ["opacity: 0.1;" if "x" in v else "" for v in s]
df.style.apply_index(highlight_x, axis="columns", level=[0, 2])
"-----"
df.dataframe(df.style.apply_index(highlight_x, axis="columns", level=[0, 2]))

def highlight_max(x, color):
   return np.where(x == np.nanmax(x.to_numpy()), f"color: {color};", None)
   
df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
df.style.apply(highlight_max, color='red')  
df.style.apply(highlight_max, color='blue', axis=1)  
st.dataframe(df.style.apply(highlight_max, color='green', axis=None)) 
df

"""
# Welcome to Streamlit1!


Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
