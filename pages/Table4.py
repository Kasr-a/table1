import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout='wide')


def fetch1():
    return pd.DataFrame({
        0: [
            'tom', 'jerry', 'diablo', 'henry'
        ],
        1: [
            20, 30, 50, 129
        ],
        2: [
            'famished', 'ecstatic', 'neurological', 'faint'
        ],
        3: [
            12, 23, 235, 121
        ],
        4: [
            'sport', 'lawyer', 'represent', 'cute'
        ],
        5: [
            44, 37, 86, 77
        ],
        6: [
            'pig', 'define', 'variable', 'sip'
        ],
        7: [
            26, 93, 27, 32
        ],
        8: [
            'grounds', 'fee', 'option', 'bus'
        ],
        9: [
            'output34', 'introduction21', 'press50', 'penalty46'
        ]
    })


def tbl_data():
    return {
        '0': 'text',
        '1': 'dropbox',
        '2': 'text',
        '3': 'dropbox',
        '4': 'dropbox',
        '5': 'dropbox',
        '6': 'text',
        '7': 'text',
        '8': 'text',
        '9': 'dropbox'
    }


def db_table():
    df = fetch1()
    colNum = len(df.columns)
    rowNum = len(df.index)
    tblFTE = tbl_data()
    colsData = {}
    rows = [st.container()]


    for curCol in range(0, colNum):
        colsData[f'{curCol}'] = df[curCol].tolist()
    for curRow in range(0, rowNum):
        rows.append(st.container())


    index = 0

    with rows[0]:
        cols = st.columns(colNum, gap='small')
        for colN in range(0, colNum):
            with cols[colN]:
                st.title(f'col {colN + 1}')
    flip = 0
    flip2 = 10
    for rowN in range(0, rowNum):

        with rows[rowN+1]:
            cols = st.columns(colNum, gap='small')
            for colN in range(0, colNum):

                with cols[colN]:

                    if tblFTE[str(colN)] == 'dropbox':
                        st.selectbox('Grid', colsData[str(colN)], label_visibility='collapsed', key=f'datapoint {index}')
                        if flip2 > 0:
                            st.markdown('##')
                            st.markdown('')
                            flip2 -= 1
                        else:
                            st.markdown('#')
                            flip2 = 10

                        index += 1
                    if tblFTE[str(colN)] == 'text':
                        st.text(colsData[str(colN)][rowN])
                        st.markdown('*****')

                        if flip == 1:
                            st.markdown('')
                            flip = 0
                        else:
                            flip = 0
                        index += 1
                    if tblFTE[str(colN)] == 'mult':
                        st.multiselect('Grid', colsData[str(colN)], label_visibility='collapsed', key=f'datapoint {index}')
                        index += 1



db_table()