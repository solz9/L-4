import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
y = st.text_input('Nhập họ và tên')
if st.button('Kết quả'):
    df = pd.read_excel('DS_10Ly4.xlsx')
    Names = df[df['Họ và tên'] == y]['Họ và tên']
    HS1 = df[df['Họ và tên'] == y]['HS1']
    BTDDS = df[df['Họ và tên'] == y]['BT01 Đúng/Sai']
    BTMM = df[df['Họ và tên'] == y]['BT02 Moment']
    Bonus = df[df['Họ và tên'] == y]['Điểm cộng']
    a = np.array([Names, HS1, BTDDS, BTMM, Bonus])
    df1 = pd.DataFrame(
        {
            "Họ và tên": a[0],
            "HS1": a[1],
            'BT01 Đúng/Sai': a[2],
            'BT02 Moment': a[3],
            'Điểm cộng': a[4]
        }
    )
    
    st.dataframe(df1)

#     st.write({'Họ và tên': Names.to_string(), 'HS1': HS1.to_string(), 'BT01 Đúng/Sai': BTDDS.to_string(), 'BT02 Moment':BTMM.to_string(), 'Điểm cộng': Bonus.to_string()})
