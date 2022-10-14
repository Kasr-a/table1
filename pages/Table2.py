import streamlit as st
import pandas as pd
import numpy as np

@st.cache(allow_output_mutation=True)
def fetch():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )


data = fetch()
st.title("Data table attempt #2")

col1, col2, col3 = st.columns(3, gap="small")

if 'right' not in st.session_state:
    st.session_state['right'] = []
if 'middle' not in st.session_state:
    st.session_state['middle'] = []
if 'left' not in st.session_state:
    st.session_state['left'] = []

with col1:
    opt1 = st.selectbox("option1", data)
    st.session_state['right'].append(opt1)

with col2:
    opt2 = st.selectbox("option2", data)
    st.session_state['middle'].append(opt1)

with col3:
    opt3 = st.selectbox("option3", data)
    st.session_state['right'].append(opt1)

opt = pd.DataFrame({"Option1": [opt1], "Option2": [opt2], "Option3": [opt3]})
st.dataframe(opt)
