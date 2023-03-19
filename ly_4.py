
import streamlit as st
import pandas as pd
import numpy as np

y = st.number_input('Nhập họ và tên')
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
if st.button('Kết quả'):
    df = pickle.load(open('ds_ly4', 'rb'))
    r = df[df['Họ và tên'] == y]['Họ và tên'], df[df['Họ và tên'] == y]['Điểm cộng'],df[df['Họ và tên'] == y]['BT01 Đúng/Sai'],df[df['Họ và tên'] == y]['BT02 Moment']
    st.write(r)

