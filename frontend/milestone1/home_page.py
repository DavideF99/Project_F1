import streamlit as st

st.title("Home page")
st.markdown("This is the home page of my F1 project. Plese select a page from the sidebar on the left or select from the links below:")
st.sidebar.markdown("Home")

st.page_link("driver_page.py", label="Link to driver page")
st.page_link("team_page.py", label="Link to team page")
st.page_link("race_page.py", label="Link to race page")
