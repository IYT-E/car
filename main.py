import streamlit as st
import datetime
from time import sleep, time

st.set_page_config(layout="wide")

st.title('カーシェアvsマイカー比較検討シミュレータ')

st.caption('各種費用やそれぞれの価値観をもとに算出します')

st.write('Current date: ', datetime.date.today())
########################################################################
st.markdown("""---""")
st.text('採用ご担当者様へ\n当サイトはAWSへのデプロイも行っておりますが、非商用かつDDoS攻撃などのリスク回避のため、今回利用した「Streamlit」ライブラリの専用デプロイサイトへデプロイしております。\n言語：Python3.9\nフレームワーク：Streamlit')

########################################################################
st.markdown("""---""")

st.header('Q1. どの車両サイズに乗っていますか/乗ることが多いですか')

car_list=['軽自動車', 'コンパクトカー（〜1000cc）', 'コンパクトカー（1001cc〜1500cc）', '小型普通車・SUV（1501cc〜2000cc）','普通車・ファミリーカー・バン（2001cc〜2500cc）']
car_tax_list_cc = [10800,29500,34500,39500,45000]
car_tax_list_g = [6600,16400,24600,24600,32800]

jibaiseki_inshi=21500

car_type = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='q1'
                )

st.text('選択中：'+car_type)
st.info('※スポーツカーや高排気量車は大手カーシェアサービスで提供されていません。\n2501cc以上の車種を希望される方は大手カーシェアではなく個人カーシェアかレンタカーになりますので本サイトでは検討対象外となります')

car_list_index=car_list.index(car_type)

st.text('現在の自動車税＝'+str(car_tax_list_cc[car_list_index]))

########################################################################
st.markdown("""---""")

st.header('Q. 車検はどの業態に頼むことが多いですか')

shaken_list=['ディーラー', '一般的な修理工場', '格安車検チェーン系']
shaken_price=[100000,50000,20000]

shaken_type = st.radio(
                  '車検請負別',
                  [i for i in shaken_list]
                )

shaken_list_index=shaken_list.index(shaken_type)
st.text('現在の車検金額＝'+str(car_tax_list_g[car_list_index]+shaken_price[shaken_list_index]+jibaiseki_inshi))


########################################################################
st.markdown("""---""")
st.header('Q. 自動車保険（任意）の金額は（年間）')

hoken_ninni=st.selectbox(
        '現在の年額もしくは新規契約をするとしたらいくらになりますか',
        [i for i in range(0,200000,1000)])

st.text('任意保険＝'+str(hoken_ninni))


########################################################################
st.markdown("""---""")
st.header('Q. ひと月にどれくらい走行しますか')
dist = st.number_input('通勤やレジャー含む全ての想定走行距離を入力してください', 0)
fuel = st.number_input('現在のガソリン価格を入力してください',min_value=0,value=150)
st.text('想定ガソリン代＝'+str(dist*fuel))
# st.text('想定移動課金代＝'+str(dist*))



########################################################################
st.markdown("""---""")
st.header('Q. カーシェアの場合、ひと月にどれくらい利用しますか')
car_dist_price=[220,220,220,330,440]
st.text('利用車種と時間の組み合わせを入力してください')


col1,col2,col3 = st.columns(3)

with col1:
    st.write('**通勤利用**')
    car_type_col1 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col1'
                )
    col1_usage = st.number_input('通勤利用日数を入力してください', 0,)

with col2:
    st.write('**週末（スポット）**')
    car_type_col2 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col2'
                )
    col2_usage = st.number_input('週末スポット利用日数を入力してください', 0,)

with col3:
    st.write('**週末（宿泊レジャー）**')
    car_type_col3 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col3'
                )
    col3_usage = st.number_input('週末宿泊レジャー利用日数を入力してください', 0,)


ex_cost=st.number_input('欄が足りない場合は以下に課金額を手動で入力してください', 0)

st.write("[参考リンクはこちら](https://share.timescar.jp/fare/use.html)")





########################################################################
st.markdown("""---""")
st.header('Q. すでにマイカーを持っていますか。もしくは新規購入しますか')

mycol1,mycol2 = st.columns(2,gap="large")

with mycol1:
    st.write('**一括購入の場合**')
    car_price = st.number_input('マイカーを持っている場合は0のままにしてください（単位：万円）',0)

with mycol2:
    st.write('**ローン購入の場合**')
    car_roan_price = st.number_input('月ごとの返済額を以下に入力してください（単位：万円）',0)



########################################################################
st.markdown("""---""")
st.header('Q. マイカーの駐車場は月額いくらかかりますか')
parking_price=st.selectbox(
        '現在の駐車場の月額もしくは想定利用月額を選択してください',
        [i for i in range(0,100000,500)])

########################################################################
st.markdown("""---""")















# # ボタンクリックはページの再読み込みトリガーとなる。
# st.button('Reload')

# # ボタンの返り値を評価する場合は、ボタンより後に条件式を記述する。
# # ボタンクリックにより、flgButton に True が格納された状態でページが再読み込みされる。
# flgButton = st.button('Switch')

# if flgButton:
#     st.balloons()