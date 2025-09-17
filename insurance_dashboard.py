# insurance_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("data/insurance_cleaned_bmi.csv")  


st.title("Medical Insurance Cost Dashboard")
st.markdown("Análise interativa de custos de seguro médico")


media_charges = df['CHARGES'].mean()
media_smoker = df[df['SMOKER']=='yes']['CHARGES'].mean()
media_nonsmoker = df[df['SMOKER']=='no']['CHARGES'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Custo Médio Mensal do Seguro", f"${media_charges:,.2f}")
col2.metric("Fumantes (Mensal)", f"${media_smoker:,.2f}")
col3.metric("Não Fumantes (Mensal)", f"${media_nonsmoker:,.2f}")


df['BMI_CAT'] = pd.cut(df['BMI'], bins=[0, 18.5, 25, 30, 100],
                       labels=['Abaixo do peso', 'Normal', 'Sobrepeso', 'Obeso'])
avg_bmi = df.groupby('BMI_CAT')['CHARGES'].mean().reset_index()
fig_bmi = px.bar(avg_bmi, x='BMI_CAT', y='CHARGES', color='BMI_CAT',
                 labels={"CHARGES":"Custo Médio ($)", "BMI_CAT":"Categoria de BMI"},
                 title="Custo Médio por Categoria de BMI")
st.plotly_chart(fig_bmi, use_container_width=True)


avg_children = df.groupby('CHILDREN')['CHARGES'].mean().reset_index()
fig_children = px.bar(avg_children, x='CHILDREN', y='CHARGES',
                      labels={"CHARGES":"Custo Médio ($)", "CHILDREN":"Número de Filhos"},
                      title="Custo Médio por Número de Filhos")
st.plotly_chart(fig_children, use_container_width=True)


st.markdown("---")
st.subheader("Segmentação de Dados")
smoker_filter = st.selectbox("Escolha status de fumante:", ['Todos', 'Sim', 'Não'])
bmi_filter = st.multiselect("Escolha categoria de BMI:",
                            ['Abaixo do peso', 'Normal', 'Sobrepeso', 'Obeso'], default=['Normal','Sobrepeso'])


df_filtered = df.copy()
if smoker_filter == 'Sim':
    df_filtered = df_filtered[df_filtered['SMOKER']=='yes']
elif smoker_filter == 'Não':
    df_filtered = df_filtered[df_filtered['SMOKER']=='no']

df_filtered = df_filtered[df_filtered['BMI_CAT'].isin(bmi_filter)]


st.dataframe(df_filtered)
