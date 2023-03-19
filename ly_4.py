install streamlit-aggrid
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
df = pd.read_excel('DS_10Ly4.xlsx')
df = pd.DataFrame(df)
df = df.drop(columns=['Họ và tên đệm', 'Tên'])
AgGrid(df)
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
a = st.number_input('Nhập họ và tên')
y = input('Họ và tên')
if st.button('Kết quả'):
  st.write(df[df['Họ và tên'] == y]['Họ và tên'], df[df['Họ và tên'] == y]['Điểm cộng'],df[df['Họ và tên'] == y]['BT01 Đúng/Sai'],df[df['Họ và tên'] == y]['BT02 Moment'])

