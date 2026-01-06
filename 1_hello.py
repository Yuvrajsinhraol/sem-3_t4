import streamlit as st
st.set_page_config(page_title='hello streamlit ',page_icon='⚾',layout='wide')
st.title("welcome to streamlit")
st.header("This is Header")
st.subheader("This is Subheader")
st.text("st.text( ) is used for simple fixed width text")
st.write("st.write()  is more flexible and can display text , number, data frames etc")
st.markdown("**st.markdown()** lets you use markdown for **rich text**")
code_example="""
def add(a,b):
    return a+b
result=add(5,7)
print(result)"""
st.code(code_example,language='python')
