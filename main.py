import streamlit as st
import pandas as pd
import numpy as np
st.title("Data table")


def fetch_data():

    return pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20))
    )


data = fetch_data()
"Choose the box you want to edit by choosing its row and column number"
row = st.number_input('row', max_value=data.shape[0])
col = st.number_input('column', max_value=data.shape[1])
"Input the new value"
val = st.number_input('value')
data.values[row][col] = val
st.dataframe(data)
