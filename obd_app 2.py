
import streamlit as st
import pandas as pd

st.title("تشخيص أعطال السيارات بالذكاء الاصطناعي 🚗🤖")

uploaded_file = st.file_uploader("حمّل ملف CSV لتشخيص الأعطال", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 بيانات السيارة:")
    st.dataframe(df.head())

    # مثال: تحليل بسيط للأعطال
    if "Error Code" in df.columns:
        st.subheader("🔍 الأعطال المكتشفة:")
        error_counts = df["Error Code"].value_counts()
        st.bar_chart(error_counts)
    else:
        st.warning("⚠️ لم يتم العثور على عمود 'Error Code' في الملف.")
else:
    st.info("⬆️ رجاءً قم بتحميل ملف CSV لبدء التشخيص.")
