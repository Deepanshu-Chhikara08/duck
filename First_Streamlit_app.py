import streamlit as st

tti = st.Page("page_1.py", title="Text GenAI Model", icon=":material/psychology:")
itt = st.Page("page_2.py", title="Text to Image Model", icon=":material/psychology:")

pg = st.navigation({
    "Text to Image":[tti, itt],
    
})

st.set_page_config(page_title="GenAI Models")
pg.run()