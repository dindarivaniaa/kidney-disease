import sys
import streamlit as st
#st.write("Python path digunakan:", sys.executable)
from streamlit_option_menu import option_menu
from web_function import load_data
from Tabs import home, predict, visualise

# Konfigurasi halaman
st.set_page_config(page_title="Prediksi Batu Ginjal", layout="wide")

# Menu Sidebar Interaktif
with st.sidebar:
    selected = option_menu(
        menu_title="Navigasi",  # Judul sidebar
        options=["Home", "Prediction", "Visualisation"],
        icons=["house", "activity", "bar-chart"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#1c1c1e"},
            "icon": {"color": "bcbcbc", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#333333",
                "color": "#eoeoeo"
            },
            "nav-link-selected": {"background-color": "#444444"},
        }
    )

# Load dataset
df, x, y = load_data()

# Panggil halaman yang sesuai
if selected == "Home":
    home.app()
elif selected == "Prediction":
    predict.app(df, x, y)
elif selected == "Visualisation":
    visualise.app(df, x, y)
