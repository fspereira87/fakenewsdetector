import streamlit as st
import os
from main import analyze_news

st.title('🕵️‍♂️ Fake News Detector')


with st.sidebar:
    st.header('🔗 Enter the Article URL')
    url = st.text_input("Article to analyse:")
    st.info("WARNING: Only English articles are supported.", icon="⚠️")

if st.button('Run analyse'):
    if not url: 
        st.error("Please fill all the fields.")
    else:
        with st.spinner('Analyzing...'):
            label, article_title = analyze_news(url)

        st.success("Analysis complete!")
        # Display the results
        st.subheader("Article Title:")
        st.write(article_title)
        
        st.subheader("🔍 Prediction:")
        st.write(f"The article is likely: **{label}**")
        #st.write(f"Prediction Score: **{score}**")