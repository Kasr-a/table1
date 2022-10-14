import streamlit as st
import pandas as pd
import numpy as np

@st.cache(allow_output_mutation=True)
def fetch():

    return pd.DataFrame(
        np.random.randn(1, 3),
        columns=('col %d' % i for i in range(20))
    )


data = fetch()
st.title("Data table attempt #2")
opt = pd.DataFrame(columns=["Option1", "Option2", "Option3"])
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    opt1 = st.selectbox("option1", data[0])
    opt.append({"Option1": opt1}, ignore_index=True)

with col2:
    opt2 = st.selectbox("option2", data[1])
    opt.append({"Option2": opt2}, ignore_index=True)

with col3:
    opt3 = st.select_box("option3", data[2])
    opt.append({"Option3": opt3}, ignore_index=True)
st.dataframe(opt)
