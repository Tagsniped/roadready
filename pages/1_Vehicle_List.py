import streamlit as st
import pandas as pd


main_string = "<h1 style=text-align:center;color:tomato>Vehicle List</h1>"
st.markdown(main_string, unsafe_allow_html=True)

df = pd.DataFrame(
    [
       {"Year": 23, "Make": "Inspection","Model": 100000,  "Color" : "John's Auto Shop", "Extra Details":"Complete"},
       {"Year": 23, "Make": "Inspection", "Model": 48967,  "Color" : "John's Auto Shop", "Extra Details":"Pending"},
       {"Year": 23, "Make": "Inspection", "Model": 84469,  "Color" : "John's Auto Shop", "Extra Details":"Complete"},
   ]
)
st.data_editor(df)