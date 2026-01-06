import streamlit as st
st.title("Text Input Demo")
name=st.text_input("ENter your name:")
comments =st.text_area("Any comments or feed back?")
st.write("**live output**")
if name:
    st.write(f"Hello: **{name}**  👋🏻")
if comments:
    st.write(f" Your comments: {comments} ")
