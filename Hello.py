import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Road Ready",
        page_icon="👋",
    )

    html_string = "<h1 style=text-align:center;color:tomato>Road Ready Tech</h1>"
    st.markdown(html_string, unsafe_allow_html=True)


    st.write("Hello and welcome to our project Road Ready Tech. This app is designed to help keep you on top of your maintenance and make sure that your vehicle is always on tip top shape. When you use our system you can rest easy knowing that your car is always Road Ready.")
    st.sidebar.success("Select a demo above.")


if __name__ == "__main__":
    run()
