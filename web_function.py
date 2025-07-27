import numpy as np 
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import streamlit as st 
import os

@st.cache()
def load_data():
    # Menghasilkan path absolut file CSV, relatif terhadap lokasi file ini.
    filepath = os.path.join(os.path.dirname(__file__), 'kidney-disease-clear.csv')
    
    # Periksa apakah file CSV tersedia.
    if not os.path.exists(filepath):
        st.error(f"File CSV tidak ditemukan di: {filepath}")
        st.stop()
    
    df = pd.read_csv(filepath)
    
    # Daftar nama kolom fitur yang harus ada di dalam CSV.
    feature_columns = ["bp", "sg", "al", "su", "rbc", "pc", "pcc", "ba",
                       "bgr", "bu", "sc", "sod", "pot", "hemo", "pcv", "wc",
                       "rc", "htn", "dm", "cad", "appet", "pe", "ane"]
    
    # Periksa apakah semua kolom fitur ada pada CSV
    if not all(col in df.columns for col in feature_columns):
        st.error("CSV tidak memiliki semua kolom fitur yang diperlukan.")
        st.stop()
    
    x = df[feature_columns]
    y = df[['classification']]
    
    return df, x, y

@st.cache
def train_model(x, y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0,
        class_weight=None,
        criterion='entropy',
        max_depth=4,
        max_features=None,
        max_leaf_nodes=None,
        min_impurity_decrease=0.0,
        min_samples_leaf=1,
        min_samples_split=2,
        min_weight_fraction_leaf=0.0,
        random_state=42,
        splitter='best'
    )
    
    model.fit(x, y)
    score = model.score(x, y)
    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)
    # Pastikan fitur diubah menjadi array numpy dan direshape menjadi baris tunggal.
    features_arr = np.array(features).reshape(1, -1)
    prediction = model.predict(features_arr)
    return prediction, score
