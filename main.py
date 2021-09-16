import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Stereamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# DF= DataFrame from pandas

st.write(df)
# st.dataframe(df)でも出来る。特徴は縦横のピクセル値（引数）を変えられる。eg. width=100, height=200.
# Doc=API reference Display data


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

"""
# Magic command
# Doc=API reference Display text

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)

# Doc=API reference Display charts

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon', ]
)

st.map(df)

# Doc=API reference Display charts

st.write('Display Image')

img = Image.open('man.png')
st.image(img, caption='No-image', use_column_width=True)

# Doc=API reference Display media
