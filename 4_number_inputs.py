import streamlit as st
st.title("Number Input & silder demo")
age=st.number_input("ENter your age:",min_value=0,max_value=100,value=25)
rating=st.slider("Rate this session(1-10):",min_value=1,max_value=10,value=5)
st.write(f"**Your age is:** {age}")
st.write(f"** YOu Rated this session :** {rating}/10")
