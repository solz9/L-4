import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
y = st.text_input('Nhập họ và tên')
if st.button('Kết quả'):
    df = pickle.load(open('ds_ly4', 'rb'))
    Names = df[df['Họ và tên'] == y]['Họ và tên']
    HS1 = df[df['Họ và tên'] == y]['HS1']
    BTDDS = df[df['Họ và tên'] == y]['BT01 Đúng/Sai']
    BTMM = df[df['Họ và tên'] == y]['BT02 Moment']
    Bonus = df[df['Họ và tên'] == y]['Điểm cộng']
    st.write(np.array([Names, HS1, BTDDS, BTMM, Bonus]).T)

