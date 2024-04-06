import streamlit as st

st.write('Test Streamlit')
st.write('Random Test')
st.title("Kalkulator Sederhana")
angka_pertama=st.number_input('masukkkan angka pertama')
st.write('the first number is', angka_pertama)

angka_kedua=st.number_input('masukkkan angka kedua')
st.write('the second number is', angka_kedua)

operasi_matematika= angka_pertama + angka_kedua
st.write(f"angka pertama {angka_pertama} x angka kedua {angka_kedua} = {operasi_matematika}")