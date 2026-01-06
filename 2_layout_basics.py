import streamlit as st
st.set_page_config(page_title='Faculty Profile ',page_icon='⚾',layout='wide')
st.title("❄ Faculty Profile Demo")
st.markdown("This example shows how to use **sidebar**,**columns**,and**ex")
st.sidebar.header("Profile Settings")
faculty_name=st.sidebar.text_input("Faculty Name",'Tejas Thakkar')
department=st.sidebar.selectbox('Department',['CE','IT','CSE','AIML'])
experience=st.sidebar.slider("Years of experience",0,40,10)
st.sidebar.markdown("---")
st.sidebar.write("You can put filters , toggle etc in sidebar")
col1,col2=st.columns([1,2])
with col1:
    st.subheader("Basic Info")
    st.write(f"**Name:** {faculty_name}")
    st.write(f"**Department:** {department}")
    st.write(f"**Experience:** {experience} years")
with col2:
    st.header("About")
    st.markdown("""Use this area to show detailed info about the faculty member,such as research intrest , publications and 
    courses handled""")
with st.expander("show courses handled "):
    st.write("Python-1")
    st.write("FSD-1")
    st.write("Digital Electronics")
    st.write("PS")
with st.expander("Show publication"):
    st.write("Paper 2024")
    st.write("Paper 2025")
