import streamlit as st

import home
import data
import plots
import predict
import about


from preprocessing import load_data
st.set_page_config(
    page_title = 'Car Price Prediction',
    page_icon = 'car',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

pages_dict = {
    "Home":home,
    "View Data": data,
    "Visualise Data": plots,
    "Predict":predict,
    "About Me":about

}
df = load_data()
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio("Go to",("Home",'View Data','Visualise Data','Predict','About Me'))
if (user_choice == "Home"):
    selected_page = pages_dict[user_choice]
    selected_page.home_app()
if (user_choice == "View Data"):
    selected_page = pages_dict[user_choice]
    selected_page.data_app(df)
if (user_choice == "Visualise Data"):
    selected_page = pages_dict[user_choice]
    selected_page.plots_app(df)
if (user_choice == "Predict"):
    selected_page = pages_dict[user_choice]
    selected_page.model_app(df)
if (user_choice == "About Me"):
    selected_page = pages_dict[user_choice]
    selected_page.about_app()            

