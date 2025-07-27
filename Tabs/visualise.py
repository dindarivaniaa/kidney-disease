import warnings
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st

from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')

    st.title("Visualisasi Model Prediksi")
    st.markdown("Lihat evaluasi dan representasi visual dari model klasifikasi yang digunakan.")
    st.markdown("---")

    with st.expander("Confusion Matrix"):
        if st.button("Tampilkan Confusion Matrix"):
            model, score = train_model(x, y)
            y_pred = model.predict(x)
            cm = confusion_matrix(y, y_pred)
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Greys', ax=ax)
            ax.set_xlabel('Prediksi')
            ax.set_ylabel('Aktual')
            ax.set_title('Confusion Matrix')
            st.pyplot(fig)
            st.markdown(f"**Akurasi Model: {score * 100:.2f}%**")

    with st.expander("Decision Tree Visualization"):
        if st.button("Tampilkan Decision Tree"):
            model, _ = train_model(x, y)
            dot_data = tree.export_graphviz(
                decision_tree=model,
                max_depth=4,
                out_file=None,
                filled=True,
                rounded=True,
                feature_names=x.columns,
                class_names=['notckd', 'ckd']
            )
            st.graphviz_chart(dot_data)

    st.markdown(
        "<div style='text-align: center; font-size: 12px; color: grey;'>© 2025 Aplikasi Prediksi Ginjal - Dibangun dengan Streamlit</div>",
        unsafe_allow_html=True
    )
