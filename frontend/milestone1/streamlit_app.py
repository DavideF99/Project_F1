import streamlit as st

# Define the pages I want 
driver_page = st.Page("driver_page.py", title="Driver Info", icon="👤")
team_page = st.Page("team_page.py", title="Team Info", icon="🏎️")
race_page = st.Page("race_page.py", title="Race Info", icon="📍")

# Set up navigation 
pages = st.navigation([driver_page, team_page, race_page])

# Run the selected page 
pages.run()