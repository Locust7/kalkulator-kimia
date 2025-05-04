import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Konsentrasi Larutan",
    page_icon="⚗",
    layout="centered"
)

# Judul utama
st.title("⚗ Kalkulator Konsentrasi Larutan")
st.markdown("""
Aplikasi ini membantu Anda menghitung berbagai jenis konsentrasi larutan:
- *PPM*
- *Molaritas*
- *Molalitas*
- *Normalitas*

Silakan pilih jenis perhitungan dan masukkan data yang diperlukan.
""")

# Pilihan jenis perhitungan
choice = st.selectbox("Pilih jenis konsentrasi yang ingin dihitung:", 
                      ["PPM (part per million)", 
                       "Molaritas (mol/L)", 
                       "Molalitas (mol/kg)", 
                       "Normalitas (N)",
                       "Molaritas (dari massa & Mr)"])

st.divider()

# Fungsi perhitungan
def hitung_ppm(massa_zat, volume_larutan):
    return (massa_zat / volume_larutan) * 1_000_000

def hitung_molaritas(mol_zat, volume_larutan):
    return mol_zat / volume_larutan

def hitung_molalitas(mol_zat, massa_pelarut):
    return mol_zat / massa_pelarut

def hitung_normalitas(ekivalen, volume_larutan):
    return ekivalen / volume_larutan

def hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan):
    mol = massa_zat / mr
    return mol / volume_larutan

# Input dan output berdasarkan pilihan
if choice == "PPM (part per million)":
    st.subheader("Perhitungan PPM")
    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("Volume larutan (liter)", min_value=0.0001, step=0.01)
    
    if st.button("Hitung PPM"):
        ppm = hitung_ppm(massa_zat, volume_larutan)
        st.success(f"Konsentrasi PPM: {ppm:.2f} ppm")

elif choice == "Molaritas (mol/L)":
    st.subheader("Perhitungan Molaritas")
    mol_zat = st.number_input("Jumlah mol zat (mol)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("Hitung Molaritas"):
        molaritas = hitung_molaritas(mol_zat, volume_larutan)
        st.success(f"Konsentrasi Molaritas: {molaritas:.2f} mol/L")

elif choice == "Molalitas (mol/kg)":
    st.subheader("Perhitungan Molalitas")
    mol_zat = st.number_input("Jumlah mol zat (mol)", min_value=0.0, step=0.01)
    massa_pelarut = st.number_input("Massa pelarut (kg)", min_value=0.0001, step=0.01)

    if st.button("Hitung Molalitas"):
        molalitas = hitung_molalitas(mol_zat, massa_pelarut)
        st.success(f"Konsentrasi Molalitas: {molalitas:.2f} mol/kg")

elif choice == "Normalitas (N)":
    st.subheader("Perhitungan Normalitas")
    ekivalen = st.number_input("Jumlah ekivalen zat (mol ekivalen)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("Hitung Normalitas"):
        normalitas = hitung_normalitas(ekivalen, volume_larutan)
        st.success(f"Konsentrasi Normalitas: {normalitas:.2f} N")

elif choice == "Molaritas (dari massa & Mr)":
    st.subheader("Perhitungan Molaritas dari Massa & Mr")
    massa_zat = st.number_input("Massa zat (gram)", min_value=0.0, step=0.01)
    mr = st.number_input("Massa molar (Mr) zat (g/mol)", min_value=0.01, step=0.01)
    volume_larutan = st.number_input("Volume larutan (liter)", min_value=0.0001, step=0.01)

    if st.button("Hitung Molaritas dari Massa"):
        molaritas_massa = hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan)
        st.success(f"Konsentrasi Molaritas: {molaritas_massa:.2f} mol/L")

