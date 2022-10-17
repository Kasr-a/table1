import streamlit as st
import pandas as pd
import numpy as np



@st.cache(allow_output_mutation=True)
def fetch1():

    return pd.DataFrame(
        np.random.randn(10, 1),
        columns=('col %d' % i for i in range(1))
    )
@st.cache(allow_output_mutation=True)
def fetch2():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )
@st.cache(allow_output_mutation=True)
def fetch3():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )
@st.cache(allow_output_mutation=True)
def fetch4():

    return pd.DataFrame(
        np.random.randn(10, 1),
        columns=('col %d' % i for i in range(1))
    )
@st.cache(allow_output_mutation=True)
def fetch5():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )
@st.cache(allow_output_mutation=True)
def fetch6():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )
@st.cache(allow_output_mutation=True)
def fetch7():

    return pd.DataFrame(
        np.random.randn(10, 1),
        columns=('col %d' % i for i in range(1))
    )
@st.cache(allow_output_mutation=True)
def fetch8():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )
@st.cache(allow_output_mutation=True)
def fetch9():

    return pd.DataFrame(
        np.random.randn(10, 3),
        columns=('col %d' % i for i in range(3))
    )


col1, col2, col3, col4 = st.columns(4, gap="small")

data1 = fetch1()
data2 = fetch2()
data3 = fetch3()
data4 = fetch4()
data5 = fetch5()
data6 = fetch6()
data7 = fetch7()
data8 = fetch8()
data9 = fetch9()

with col1:
    st.header("col1")
    opt11 = st.selectbox("", data1, label_visibility='collapsed')
    opt12 = st.selectbox("", data2, label_visibility='collapsed')
    opt13 = st.selectbox("", data3, label_visibility='collapsed')

with col2:
    st.header("col2")
    opt21 = st.selectbox("", data4, label_visibility='collapsed')
    opt22 = st.selectbox("", data5, label_visibility='collapsed')
    opt23 = st.selectbox("", data6, label_visibility='collapsed')

with col3:
    st.header("col3")
    opt31 = st.selectbox("", data7, label_visibility='collapsed')
    opt32 = st.selectbox("", data8, label_visibility='collapsed')
    opt33 = st.selectbox("", data9, label_visibility='collapsed')

with col4:
    st.header("col4")
    opt41 = opt11 * opt21 + opt31
    opt42 = opt12 * opt22 + opt32
    opt43 = opt13 * opt23 + opt33
    opt41
    opt42
    opt43
