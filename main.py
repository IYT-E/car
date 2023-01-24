import streamlit as st
import datetime
import math
from time import sleep, time

st.set_page_config(layout="wide")

st.title('カーシェアvsマイカー比較検討シミュレータ')

st.text('各種費用やそれぞれの価値観をもとに算出します。\n・すでにマイカーを持っていてカーシェアの利用を検討している方\n・マイカー未所持で購入かカーシェアか比較したい方')

st.write('Current date: ', datetime.date.today())
########################################################################
st.markdown("""---""")
st.text('採用ご担当者様へ\n当サイトはAWSへのデプロイも行っておりますが、非商用かつDDoS攻撃などのリスク回避のため、\n今回利用したWebフレームワーク「Streamlit」の専用デプロイサイトへデプロイしております。\n\n言語：Python3.9\nフレームワーク：Streamlit')

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

# st.text('現在の自動車税＝'+str(car_tax_list_cc[car_list_index]))

########################################################################
st.markdown("""---""")

st.header('Q2. 車検はどの業態に頼むことが多いですか/頼みそうですか')

shaken_list=['ディーラー', '一般的な修理工場', '格安車検チェーン系']
shaken_price=[100000,50000,20000]

shaken_type = st.radio(
                  '車検請負別',
                  [i for i in shaken_list]
                )

shaken_list_index=shaken_list.index(shaken_type)
shaken_once_price=car_tax_list_g[car_list_index]+shaken_price[shaken_list_index]+jibaiseki_inshi
# st.text('現在の車検金額＝'+str(shaken_once_price))
shaken_year_price=shaken_once_price//2


########################################################################
st.markdown("""---""")
st.header('Q3. 自動車保険（任意）の金額は（年間）')

hoken_ninni=st.selectbox(
        '現在の年額もしくは新規契約をするとしたらいくらになりますか',
        [i for i in range(0,200000,1000)])

# st.text('任意保険＝'+str(hoken_ninni))


########################################################################
st.markdown("""---""")
st.header('Q4. ひと月にどれくらい走行しますか')
dist = st.number_input('通勤やレジャー含む全ての想定走行距離を入力してください（単位：km）', 1)
nenpi= st.number_input('燃費（km/l）を入力してください', 1.0)
fuel = st.number_input('現在のガソリン価格を入力してください',min_value=0,value=150)
gas=math.floor(dist/nenpi*fuel)
st.text('想定ガソリン代＝'+str(gas))
# st.text('想定移動課金代＝'+str(dist*))



########################################################################
st.markdown("""---""")
st.header('Q5. カーシェアの場合、ひと月にどれくらい利用しますか')
st.text('利用車種と時間の組み合わせを入力してください')

col1,col2,col3 = st.columns(3)

with col1:
    st.write('**通勤・レジャーデイユース（11時間利用想定）**')
    car_type_col1 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col1'
                )
    col1_usage = st.number_input('通勤・レジャーの利用日数を入力してください', 0,)

with col2:
    st.write('**6H以下のスポット利用**')
    car_type_col2 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col2'
                )
    col2_usage = st.number_input('スポット利用日数を入力してください', 0,)

with col3:
    st.write('**24H以上のレジャーなどでの利用**')
    car_type_col3 = st.radio(
                  label='車両サイズを選んでください',
                  options=[i for i in car_list],
                  key='col3'
                )
    col3_usage = st.number_input('24H以上の利用日数を入力してください', 0,)


ex_cost=st.number_input('欄が足りない場合は以下に課金額を手動で入力してください', 0)

st.write("[参考リンクはこちら](https://share.timescar.jp/fare/use.html)")

col1_dist=0
col3_dist=0

if col1_usage+col2_usage+col3_usage != 0:
    usage_sum=col1_usage+col2_usage+col3_usage
    col1_dist = dist/usage_sum*col1_usage
    col3_dist = dist/usage_sum*col3_usage

col1_price_list=[5500,5500,5500,7700,9900]
col2_price_list=[220,220,220,330,440]
col3_price_list=[6600,6600,6600,8800,12100]

col1_price = (col1_usage*(col1_price_list[car_list.index(car_type_col1)]) + (col1_dist*16))*12
col2_price = (col2_usage*(col2_price_list[car_list.index(car_type_col2)]) * 12)*12
col3_price = (col3_usage*(col3_price_list[car_list.index(car_type_col3)]) + (col3_dist*16))*12


########################################################################
st.markdown("""---""")
st.header('Q6. すでにマイカーを持っていますか。もしくは新規購入しますか')

mycol1,mycol2 = st.columns(2,gap="large")

with mycol1:
    st.write('**一括購入の場合**')
    car_price = st.number_input('残債のないマイカーを持っている場合は0のままにしてください（単位：円）',0)

with mycol2:
    st.write('**ローン購入の場合（新規契約もしくは返済中）**')
    car_loan_price = st.number_input('月ごとの返済額を以下に入力してください（単位：円）',0)



########################################################################
st.markdown("""---""")
st.header('Q7. マイカーの駐車場は月額いくらかかりますか')
parking_price=st.selectbox(
        '現在の駐車場の月額もしくは想定利用月額を選択してください（単位：円）',
        [i for i in range(0,100000,500)])

########################################################################
st.markdown("""---""")
st.header('Q8. マイカーの部品やメンテナンス関連にはどれくらいコストをかけますか')
men_list=['じっくり豪華にこだわって', '多少高グレードに','ディーラーまかせ','安すぎず高すぎず', '常に値段重視']
men_price_list=[100000,75000,50000,35000,20000]
men_select=st.radio('例：タイヤのグレード、洗車関連、オイル交換、ゴムまわりなど予防保守',
                    [i for i in men_list])
men_price=men_price_list[men_list.index(men_select)]

########################################################################
st.markdown("""---""")
st.header('Q9. 以下の要素にはどれくらいの金銭的価値観（年間）がありますか')
st.text('なんとなくのフィーリングで結構です。\nいずれも単位は万円です。\nプラスのみ、マイナスのみの数字に設定可能な項目もありますのでご注意ください。')
st.write('**マイカー編**')
car_f_1 = st.number_input('いつでも使いたいときに利用できる（単位：万円）',0)
car_f_2 = st.number_input('車内外を自由にカスタマイズできる（小物や装飾品、車中泊仕様化など）（単位：万円）',0)
car_f_3 = st.number_input('1つの車両を運転し続けることによって得られる車幅感覚などの安定感（単位：万円）',0)
car_f_4 = st.number_input('車検や消耗品等の交換系作業の手配、洗車などで自らの時間が割かれることに対する金銭的損失（単位：万円）',min_value=-1000000,value=0, max_value=0)
car_f_5 = st.number_input('万が一の盗難や事故など、保険に入っていたとしても被る時間的・精神的ダメージ（単位：万円）',min_value=-1000000,value=0, max_value=0)
car_f_6 = st.number_input('ほか、マイカーに感じる要素（単位：万円）',min_value=-1000000,value=0)
car_f_sum=(0-car_f_1-car_f_2-car_f_3)-(car_f_4+car_f_5+car_f_6)


st.write('**カーシェア編**')
cars_f_1 = st.number_input('毎回の利用予約作業の手間（単位：万円）',min_value=-1000000,value=0,max_value=0)
cars_f_2 = st.number_input('使いたいときに最寄りの駐車場に使える車両がない場合の時間的・金銭的ダメージ（単位：万円）※カーシェアマップはページ最下部に掲載',min_value=-1000000,value=0,max_value=0)
cars_f_3 = st.number_input('車内外を自由にカスタマイズできない（小物や装飾品、車中泊仕様化など）、ペットやタバコNGなこと（単位：万円）',min_value=-1000000,value=0,max_value=0)
cars_f_4 = st.number_input('ほか、カーシェアに感じる要素（単位：万円）',min_value=-1000000,value=0)
cars_f_sum=0-(cars_f_1+cars_f_2+cars_f_3)-cars_f_4

########################################################################
st.markdown("""---""")
st.header('質問をもとに算出したマイカーとカーシェアの比較グラフ')

str_tmp='''
【変数等一覧】
マイカー
1，2，3，4，6，7，8，9
カーシェア
4(4+5),5,9

1自動車税
car_tax_list_cc[car_list_index]

2 車検年額
shaken_year_price

3 任意保険
hoken_ninni

4 想定ガソリン代
gas

5 カーシェアの場合、ひと月にどれくらい利用しますか
 distを3項目で按分する
 1と3については時間と距離課金
 2は時間課金

6 一括購入は初年度ぶんにまるまる、ローンは＊12して年額扱い
car_price
car_loan_price

7 駐車場
parking_price

8 メンテナンス
men_price

9 自由入力欄
car_f_sum マイカー
cars_f_sum カーシェア


'''

# マイカー年額合計
mycar_total=car_tax_list_cc[car_list_index]+car_tax_list_g[car_list_index]+shaken_year_price+hoken_ninni+gas+(car_loan_price*12)+parking_price+men_price+car_f_sum


st.write('**マイカー暫定合計 一括購入費用除く**')
st.write('**月額：**',f'{mycar_total//12}','円')
st.write('**年額：**',f'{mycar_total}','円')

# カーシェア年額合計
carshare_total= col1_price+col2_price+col3_price+cars_f_sum

st.write('**カーシェア暫定合計**')
st.write('**月額：**',f'{math.floor(carshare_total//12)}','円')
st.write('**年額：**',f'{math.floor(carshare_total)}','円')


st.write('グラフ化は工事中')




########################################################################
st.markdown("""---""")
st.header('参考：カーシェアマップ')
st.write('工事中')


# # ボタンクリックはページの再読み込みトリガーとなる。
# st.button('Reload')

# # ボタンの返り値を評価する場合は、ボタンより後に条件式を記述する。
# # ボタンクリックにより、flgButton に True が格納された状態でページが再読み込みされる。
# flgButton = st.button('Switch')

# if flgButton:
#     st.balloons()