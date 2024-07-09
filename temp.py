import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('creditcard.csv')
df_head = df.head()
df_null = df.isna().sum().sort_values(ascending = False)
nulls = pd.DataFrame(df_null, columns = ['Null count'])
total = df.isnull().sum().sort_values(ascending = False)
percent = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
percentage = pd.concat([total, percent], axis=1, keys=['Total', 'Percent']).transpose()
class_ = df['Class'].value_counts()
class_df = pd.DataFrame({'Class': class_.index,'values': class_.values})


import streamlit as st

st.title("임시적으로 만들어본 사이트")
st.header("카드 사기에 대한 소량의 미리보기")

st.write("먼저 데이터의 구조를 알아보겠습니다.")

st.dataframe(df_head)

st.write("훈련 목표는 Class 열의 0과 1로써 Not Fraud와 Fraud로 결과를 확인할 수 있겠습니다.")


st.write("현재 보고있는 데이터는 결측치가 0에 수렴한다는 점을 확인할 수 있습니다.")
st.dataframe(nulls)

st.write("그럼 타겟값인 Class의 비율을 확인해보겠습니다.")
st.bar_chart(class_df.set_index('Class'))
st.write("사기건수의 개수는 492 (0.172%)라고 합니다.")