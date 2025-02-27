import streamlit as st
from PIL import Image

st.title(" Mi primera cosa")

st.header("Una caraca re chida.")
st.write("Si que estamos chida!!!")
image = Image.open("armydark5.jpg")

st.image(image, caption="Interfaces multimodales")


texto = st.text_input("Escribe algo", "Este es mi texto")
st. write("El texto escrito es", texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es una columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")
