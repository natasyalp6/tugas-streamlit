import streamlit as st
import statistics

def main():
    st.title("WELCOME TO MY STREAMLIT TEMAN TEMAN")
    st.write("YUK ISI REGISTRASI DULU NICH BIAR MAKIN KENAL !")

    # Menambahkan input teks
    name = st.text_input("Masukkan nama kamu donggg:")
    NRP = st.text_input("Masukkan NRP kamu donggg yang lengkap ya:")
    ANGKATAN = st.text_input("Masukkan ANGKATAN kamu donggg yang lengkap ya:")
    Alamat = st.text_input("Masukkan alamat kamu donggg yang lengkap ya:")

    # Menambahkan tombol
    button = st.button("REGISTRATION")

    # Menambahkan tindakan saat tombol diklik
    if button:
        st.write(f"HALOOO, {name} DENGAN NRP {NRP} KAMU SUDAH OFFICIALLY JOIN DI MY STREAMLIT ")
        st.write(f"SELAMAT YAAA, {name} DENGAN NRP {NRP} ")
        st.write(f"KAMU ANGKATAN, {ANGKATAN} dan tinggal di {Alamat}  WAH SEMANGAT YAAA")
        st.write(f"YUHUY!!!, {name} SEKARANG WAKTUNYA BELAJAR SILAHKAN NIKMATI BERBAGAI FITURNYA YAWW")
        st.write(f"FIGHTING, {name} JANGAN MALAS YAAA")


    st.title("Perhitungan Statistik Lengkap")
    st.write(" Sekarang kita belajar statistika deskriptif yaaa!")
    st.write(" Masukkan angka-angka yang ingin dihitung statistiknya yaaa gk usah tegang!") 

    # Menambahkan input teks
    angka = st.text_input("Masukkan angka jangan lupa dipisahkan oleh koma:", "")

    # Mengonversi input menjadi list angka
    angka_list = [float(x.strip()) for x in angka.split(",") if x.strip()]

    # Menghitung statistik
    if angka_list:
        rata_rata = statistics.mean(angka_list)
        median = statistics.median(angka_list)
        deviasi_standar = statistics.stdev(angka_list)

        st.write(f"Rata-rata: {rata_rata}")
        st.write(f"Median: {median}")
        st.write(f"Deviasi Standar: {deviasi_standar}")

if __name__ == "__main__":
    main()
import streamlit as st
import scipy.stats as stats

def main():
    st.title("Analisis Variansi (ANOVA)")
    st.write("Masukkan data kelompok yang ingin kamu analisis nich")

    # Menambahkan input teks
    data_group1 = st.text_input("Masukkan data kelompok 1 jangan lupa pisahkan koma:", "")
    data_group2 = st.text_input("Masukkan data kelompok 2 jangan lupa pisahkan oleh koma:", "")
    data_group3 = st.text_input("Masukkan data kelompok 3 jangan lupa pisahkan koma:", "")

    # Mengonversi input menjadi list angka
    group1 = [float(x.strip()) for x in data_group1.split(",") if x.strip()]
    group2 = [float(x.strip()) for x in data_group2.split(",") if x.strip()]
    group3 = [float(x.strip()) for x in data_group3.split(",") if x.strip()]

    # Mengecek apakah data lengkap untuk analisis
    if len(group1) > 1 and len(group2) > 1 and len(group3) > 1:
        # Menggunakan fungsi f_oneway dari modul stats
        f_statistic, p_value = stats.f_oneway(group1, group2, group3)

        st.write("Hasil Analisis:")
        st.write("Nilai F-statistic:", f_statistic)
        st.write("Nilai p-value:", p_value)

if __name__ == "__main__":
    main()
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    st.title("Perhitungan Regresi")
    st.write("Masukkan data X dan Y untuk melakukan perhitungan regresi jangan tegang yaaa")

    # Menambahkan input teks
    data_x = st.text_input("Masukkan data X dipisahkan oleh koma:", "")
    data_y = st.text_input("Masukkan data Y dipisahkan oleh koma:", "")

    # Mengonversi input menjadi list angka
    x = np.array([float(val) for val in data_x.split(",") if val.strip()])
    y = np.array([float(val) for val in data_y.split(",") if val.strip()])

    # Mengecek apakah data lengkap untuk perhitungan regresi
    if len(x) > 1 and len(y) > 1 and len(x) == len(y):
        # Mengubah dimensi data X menjadi bentuk yang sesuai
        x = x.reshape(-1, 1)

        # Membuat model regresi linear
        reg = LinearRegression()
        reg.fit(x, y)

        # Mendapatkan koefisien regresi
        coef = reg.coef_[0]
        intercept = reg.intercept_

        st.write("Hasil Perhitungan Regresi:")
        st.write(f"Persamaan Regresi: Y = {coef:.2f} * X + {intercept:.2f}")

if __name__ == "__main__":
    main()
