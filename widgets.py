import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive widgets')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味:', text

if st.checkbox('Show Image'):
        img = Image.open('man.png')
        st.image(img, caption=' man', use_column_width=True)

option = st.selectbox(
        'あなたの好きな数字を教えてください',
        list(range(1, 11))
)

'あなたの好きな数字は、', option,'です。'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション', condition

# チェックボックス、セレクトボックス、テキスト、スライダーの４つやった。動的に値を変化するもの。
# Doc = API reference Display interactive widgets