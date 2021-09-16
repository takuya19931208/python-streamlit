import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive widgets')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')


text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味:', text
'コンディション', condition


# サイドバーの追加、２カラムレイアウト、エクスパンダー
