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
    st.write(np.array({'Họ và tên':[Names], 
                       'HS1': [HS1], 
                       'BT01 Đúng/Sai':[BTDDS], 
                       'BT02 Moment': [BTMM],
                       'Điểm cộng': [Bonus]}))

# "name": ["An", "Bình", "Châu", "Nam", "Mai"], 
#     "grade": [7, 6, 5, 7, 9], 
#     "class": ["10A1", "10A2", "10A3", "10B", "10C"],
#     "gender": ["Nữ", "Nam", "Nam", "Nam", "Nữ"]
# }
