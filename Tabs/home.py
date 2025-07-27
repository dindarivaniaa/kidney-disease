import streamlit as st

def app():
    # Custom style untuk latar dan teks utama
    st.markdown("""
        <style>
        .main {
            background-color: #1e1e1e;
            color: #e0e0e0;
        }
        h1, h2, h3, h4 {
            color: #f0f0f0;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Aplikasi Prediksi Penyakit Batu Ginjal")
    st.markdown("---")

    st.markdown("""
    #### Tentang Aplikasi
    Aplikasi ini dikembangkan untuk membantu memprediksi potensi penyakit batu ginjal berdasarkan data laboratorium pasien, menggunakan algoritma **Decision Tree**.

    Tujuan dari aplikasi ini adalah memberikan **alat bantu** yang praktis dan cepat bagi tenaga medis atau peneliti untuk menilai kemungkinan pasien terkena batu ginjal.
    """)

    st.markdown("#### Fitur Utama")
    st.markdown("""
    - **Prediction** — Form input untuk memprediksi kondisi pasien.
    - **Visualisation** — Menampilkan pohon keputusan dan confusion matrix.
    - **Evaluasi Model** — Akurasi dan performa model berdasarkan dataset.

    """)

    st.markdown("#### Petunjuk Penggunaan")
    st.markdown("""
    1. Buka menu **Prediction** di sidebar.
    2. Isi seluruh data laboratorium sesuai format.
    3. Klik tombol *Prediksi* dan lihat hasilnya.
    4. Buka menu **Visualisation** untuk melihat evaluasi model.

    """)

    st.markdown("---")
    st.info("🛠 Versi : 1.0 | 👨‍💻 Developer : Dinda Rivania")

    st.markdown(
        "<div style='text-align: center; font-size: 12px; color: grey;'>© 2025 Aplikasi Prediksi Ginjal - Dibangun dengan Streamlit</div>",
        unsafe_allow_html=True
    )
