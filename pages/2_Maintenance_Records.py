
import streamlit as st
import pandas as pd
import datetime


main_string = "<h1 style=text-align:left;color:tomato>Maintenance Records</h1>"
st.markdown(main_string, unsafe_allow_html=True)

#st.title("Maintenance Test")

df = pd.DataFrame(
    [
       {"Date": datetime.date(2023, 12, 12), "Service": "Inspection","Odometer#": 100000,  "Company" : "John's Auto Shop", "Status":"Complete"},
       {"Date": datetime.date(2023, 12, 12), "Service": "Inspection", "Odometer#": 48967,  "Company" : "John's Auto Shop", "Status":"Pending"},
       {"Date": datetime.date(2023, 12, 12), "Service": "Inspection", "Odometer#": 84469,  "Company" : "John's Auto Shop", "Status":"Complete"},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic", hide_index=True)
