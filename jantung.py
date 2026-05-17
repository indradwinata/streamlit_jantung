import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import pickle
import joblib

st.title("Aplikasi Skrining Prediksi Penyakit Jantung")
st.write("Halo! Selamat datang di aplikasi skrining prediksi penyakit jantung by @indrawinata")
st.sidebar.header("Page sidebar")
st.sidebar.image("jantung.jpg")
sidebar = st.sidebar.selectbox(
    "The app features",
    ("Halaman utama", "Analisis", "Cek Risiko anda")
)


if sidebar == "Halaman utama":
    st.header("Apa itu Penyakit Jantung?")

    st.write("""Penyakit jantung adalah istilah umum yang digunakan untuk menggambarkan berbagai gangguan pada jantung dan pembuluh darah.
    Salah satu jenis yang paling sering terjadi adalah penyakit jantung koroner, yaitu kondisi ketika pembuluh darah yang memasok darah ke otot jantung jantung mengalami penyempitan atau penyumbatan akibat penumpukan lemak dan kolesterol (plak).
    Kondisi ini dapat mengurangi aliran darah dan oksigen ke jantung sehingga meningkatkan risiko nyeri dada, serangan jantung, gagal jantung, hingga kematian.""")

    st.image("gejala2.jpg")
    st.subheader("Gejala Penyakit Jantung")

    st.write("""
            Gejala utama Penyakit Jantung antara lain :

- Nyeri atau rasa tidak nyaman di dada
- Sesak napas, terutama saat aktivitas
- Jantung berdebar atau denyut tidak teratur
- Mudah lelah
- Pusing atau kehilangan kesadaran
- Nyeri yang menjalar ke lengan, leher, rahang, atau punggung
- Pembengkakan pada kaki atau pergelangan kaki
- Keringat dingin dan mual
""")

    st.subheader("Faktor Risikonya apa saja?")

    st.write("""
    Penyakit jantung dipengaruhi oleh kombinasi faktor biologis, perilaku, dan lingkungan. Faktor risiko utama meliputi:

Faktor Risiko yang Tidak Dapat Diubah
- Usia yang semakin bertambah
- Jenis kelamin laki-laki memiliki risiko lebih tinggi pada usia produktif
- Riwayat keluarga dengan penyakit jantung
- Faktor genetik atau keturunan

Faktor Risiko yang Dapat Diubah
-Tekanan darah tinggi (hipertensi)
-Kolesterol tinggi
-Diabetes mellitus
-Merokok
-Obesitas atau kelebihan berat badan
-Kurang aktivitas fisik
-Pola makan tinggi lemak, gula, dan garam
-Konsumsi alkohol berlebihan
-Stres berkepanjangan
-Kurang tidur dan gaya hidup sedentari

Sebagian besar faktor risiko tersebut sebenarnya dapat dicegah atau dikendalikan melalui perubahan gaya hidup sehat dan pemeriksaan kesehatan secara rutin.""")

    st.subheader("Pencegahan dan Pengobatan Penyakit Jantung")

    st.write("""
        Pencegahan penyakit jantung dapat dilakukan sejak dini melalui penerapan gaya hidup sehat, antara lain:

- Mengonsumsi makanan bergizi seimbang
- Memperbanyak buah dan sayur
- Mengurangi makanan tinggi lemak jenuh, gula, dan garam
- Berolahraga secara rutin minimal 150 menit per minggu
- Tidak merokok dan menghindari paparan asap rokok
- Menjaga berat badan ideal
- Mengelola stres dengan baik
- Memeriksa tekanan darah, gula darah, dan kolesterol secara berkala
Pengobatan penyakit jantung bergantung pada jenis dan tingkat keparahan penyakit.
Penanganan dapat berupa perubahan gaya hidup, pemberian obat-obatan, hingga tindakan
medis seperti pemasangan stent, operasi bypass jantung, atau prosedur lainnya.
Deteksi dini sangat penting agar penanganan dapat dilakukan lebih cepat dan risiko komplikasi dapat diminimalkan.
""")

    st.subheader("Pentingnya Deteksi Dini dengan Aplikasi Prediksi Penyakit Jantung")

    st.write("""
        Banyak kasus penyakit jantung berkembang secara perlahan tanpa gejala yang jelas pada tahap awal.
        Oleh karena itu, deteksi dini menjadi langkah penting untuk mengidentifikasi individu yang memiliki risiko tinggi sebelum terjadi komplikasi serius.
        Aplikasi prediksi penyakit jantung ini dikembangkan untuk membantu masyarakat mengenali tingkat risiko
        penyakit jantung berdasarkan faktor-faktor kesehatan dan gaya hidup yang dimiliki. Dengan memanfaatka
        teknologi dan analisis data, aplikasi ini diharapkan dapat meningkatkan kesadaran masyarakat terhadap kesehatan jantung,
        mendorong pemeriksaan kesehatan lebih lanjut, serta mendukung upaya pencegahan penyakit jantung secara lebih cepat, mudah, dan efektif.""")


if sidebar == "Analisis":

    st.header("Analysis")
    st.write("Insights dataset")


    st.image("img/output1.png")
    st.write("*Grafik 1. DIstribusi perbandingan variabel numerik (umur, blood presuare(bps), Kolestrol (chol),Thalac,oldpeak berdasarkan kategori penyakit jantung *")

    st.image("img/output2.png")
    st.write("*Grafik 2. Distribusi perbandingan variabel berdasarkan kategori penyakit jantung *")

    st.image("img/output3.png")
    st.write("*Grafik 3. Hasil analisis korelasi antar variabel *")

    st.image("img/output4.png")
    st.write("*Grafik 4. Distribusi data variabel numerik yang dianalisis *")

if sidebar == "Cek Risiko anda":
    st.header("Cek risiko anda")
    st.write("*Seberapa besar risiko anda mengalami penyakit jantung*")

    img = Image.open("jantung.jpg")
    st.image(img, width=500)

    st.subheader("Isi Informasi Berikut")

    sex_option = st.selectbox("Jenis Kelamin", ('Perempuan', 'Pria'))
    if sex_option == 'Perempuan':
        sex = 0
    else:
        sex = 1
    age = st.slider("Usia", 29, 77, 30)
    cp = st.slider('Chest pain type', 1,4,2)
    if cp == 1.0:
        wcp = "Nyeri dada tipe angina"
    elif cp == 2.0:
        wcp = "Nyeri dada tipe nyeri tidak stabil"
    elif cp == 3.0:
        wcp = "Nyeri dada tipe nyeri tidak stabil yang parah"
    else:
        wcp = "Nyeri dada yang tidak terkait dengan masalah jantung"
    st.write("Jenis nyeri dada yang dirasakan oleh pasien", wcp)

    thalach = st.slider("Maximum heart rate achieved", 71, 202, 80)
    slope = st.slider("Kemiringan segmen ST pada elektrokardiogram (EKG)", 0, 2, 1)

    exang = st.selectbox("Apakah ada rasa sakit saat berolahraga, melakukan latihan ringan?, 1=ya, 0=tidak", (0, 1))
    oldpeak = st.slider("Seberapa banyak ST segmen menurun atau depresi", 0.0, 6.2, 1.0)
    ca = st.slider("Number of major vessels", 0, 3, 1)
    thal = st.slider("Hasil tes thalium", 1, 3, 1)



    # Changed from st.sidebar.button to st.button for main page placement
    if st.button('klik prediksi!'): # Changed button text back to 'klik prediksi!' as per previous request

        df = pd.DataFrame([{
            'age': age,
            'sex': sex,
            'cp': cp,
            'thalach': thalach,
            'slope': slope,
            'exang': exang,
            'oldpeak': oldpeak,
            'ca': ca,
            'thal': thal
        }])

        with open("model_rf_jantung.pkl", 'rb') as file:
            loaded_model = pickle.load(file)
        prediction = loaded_model.predict(df)[0]
        st.subheader('Prediction: ')
        with st.spinner('Wait for it...'):
            time.sleep(4)
            # Conditional coloring for prediction message
            if prediction == 0:
                st.success("Alhamdulillah tidak berisiko")
            else:
                st.error("HATI-HATI ANDA BERISIKO JANTUNG")
