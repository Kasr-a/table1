import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def fetch1():

    return pd.DataFrame(
        np.random.randn(20, 50),
        columns=('col %d' % i for i in range(50))
    )


df = fetch1()
colNum = len(df.columns)
colsData = {}
for curCol in range(0, colNum):
    colsData[f'{curCol}'] = df[f'col {curCol}'].tolist()

col = st.columns(colNum, gap='small')
index = 0

for colN in range(0, colNum):
    with col[colN]:
        for data in colsData.values():
            st.selectbox("Grid", data, label_visibility='collapsed', key=f'datapoint {index}')
            index += 1