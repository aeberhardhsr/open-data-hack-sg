from datetime import datetime
import streamlit as st
import time



st.title("Verkehrszählungen St. Gallen")
st.write("Here you can answer to some questions in this form")

user_id = st.text_input("ID", value="", max_chars=7)

info = st.text_area("Share some information about you", "Put information here", help="you can write about yourself")

age = st.number_input("Age", min_value=18, max_value=100, step=1)

date = st.date_input("select your birthday")

alert_time = st.time_input("Wake up time")

smoke = st.checkbox("Do you smoke?")
genre = st.radio("Which movie genre do you like?", options=["horror", "adventure", "romantic"])

weight = st.slider("choose your weight", min_value=40., max_value=150., step=0.5)

physical_form = st.selectbox("select level of physical condition", options=["bad", "normal", "good"])
colors = st.multiselect("what are your favorite colors?", options=["green", "red", "yellow", "pink"])

image = st.file_uploader("upload your photo", type=["jpg", "png"])

submit = st.button("submit")

if submit:
    st.write("you submitted the form")

st.sidebar.write("hello from the sidebar")
click = st.sidebar.button("click me")
if click:
    st.sidebar.write("you clicked meh")


col1, col2 = st.columns(2)
with col1:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.button("like cats")
with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg", width=300)
    st.button("like dogs")

    st.metric("my metric", 42,2)


size = st.select_slider("pick a size", ["S", "M", "L"])

c = st.container()
st.write("this will show last")
c.write("this will show first")
c.write("whis will show second")

with st.form(key="myform"):
    username = st.text_input("username")
    password = st.text_input("password")
    st.form_submit_button("login")