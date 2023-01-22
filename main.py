import streamlit as st
import datetime
from time import sleep, time


st.title('カーシェアvsマイカー比較検討')
st.caption('Webアプリテスト')

st.write('### Current date: ', datetime.date.today())

# ボタンクリックはページの再読み込みトリガーとなる。
st.button('Reload')

# ボタンの返り値を評価する場合は、ボタンより後に条件式を記述する。
# ボタンクリックにより、flgButton に True が格納された状態でページが再読み込みされる。
flgButton = st.button('Switch')

if flgButton:
    st.balloons()