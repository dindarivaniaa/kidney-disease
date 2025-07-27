import streamlit as st 
from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi Pasien")
    st.markdown("---")
    st.markdown("Silakan masukan nilai-nilai hasil laboratorium pasien di bawah ini (dalam format angka):")

    col1, col2 = st.columns(2)

    with col1:
        bp = st.text_input("Tekanan darah (bp)")
        sg = st.text_input("Specific Gravity (sg)")
        al = st.text_input("Albumin (al)")
        su = st.text_input("Sugar (su)")
        rbc = st.text_input("Red blood cells (rbc)")
        pc = st.text_input("Pus cell (pc)")
        pcc = st.text_input("Pus cell clumps (pcc)")
        ba = st.text_input("Bacteria (ba)")
        bgr = st.text_input("Blood glucose random (bgr)")
        bu = st.text_input("Blood urea (bu)")
        sc = st.text_input("Serum creatinine (sc)")

    with col2:
        sod = st.text_input("Sodium (sod)")
        pot = st.text_input("Potassium (pot)")
        hemo = st.text_input("Hemoglobin (hemo)")
        pcv = st.text_input("Packed cell volume (pcv)")
        wc = st.text_input("White blood cell count (wc)")
        rc = st.text_input("Red blood cell count (rc)")
        htn = st.text_input("Hypertension (htn)")
        dm = st.text_input("Diabetes mellitus (dm)")
        cad = st.text_input("Coronary artery disease (cad)")
        appet = st.text_input("Appetite (appet)")
        pe = st.text_input("Pedal edema (pe)")
        ane = st.text_input("Anemia (ane)")

    # Gabungkan semua input
    inputs = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc,
              sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    st.markdown("---")

    # Tombol prediksi
    if st.button("Prediksi Sekarang"):
        try:
            # Konversi semua input ke float
            numeric_features = [float(val) for val in inputs]

            prediction, score = predict(x, y, numeric_features)
            st.success("✅ Prediksi berhasil dilakukan.")

            st.markdown("### Hasil Prediksi")
            if prediction == 1:
                st.warning("⚠️ Pasien kemungkinan **rentan terkena batu ginjal**.")
            else:
                st.info("✅ Pasien kemungkinan **tidak terkena penyakit batu ginjal**.")

            st.markdown(f"Tingkat akurasi model: **{score * 100:.2f}%**")
        
        except ValueError:
            st.error("❌ Semua input harus berupa angka. Silakan periksa kembali.")

    st.markdown(
        "<div style='text-align: center; font-size: 12px; color: grey;'>© 2025 Aplikasi Prediksi Ginjal - Dibangun dengan Streamlit</div>",
        unsafe_allow_html=True
    )
