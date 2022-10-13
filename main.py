import streamlit as st
import pandas as pd
import numpy as np
st.title("Data table")
data = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20))
)
val = st.number_input('value')
row = st.number_input('row', max_value=data.shape[0])
col = st.number_input('column', max_value=data.shape[1])
data.values[row][col] = val
st.dataframe[data]
