import streamlit as st
import pandas as pd
import numpy as np
st.title("Data table attempt #1")

@st.cache(allow_output_mutation=True)
def fetch_data():

    return pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20))
    )


"Choose the box you want to edit by choosing its row and column number"
col1, col2 = st.columns(2, gap="small")
col3, valcol = st.columns(2, gap="small")
data = fetch_data()

with col1:
    row = st.number_input('row', max_value=data.shape[0])
with col2:
    col = st.number_input('column', max_value=data.shape[1])
with col3:
    st.markdown("Input the new value")
with valcol:
    val = st.number_input('value')
data.loc[row][col] = val
st.dataframe(data)
