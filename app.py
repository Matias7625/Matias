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

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual", "auditiva", "tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Audítiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de botones")
if st.button("Presiona el boton"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aun")

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Seleciona la modalidad",
  ("Audío", "Visual", "Háptico"),

)
if in_mod == "Audío":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Haptico":
  set_mod = "Activar vibracion"
st.write("La accion es:" , set_mod)


with st.sidebar:
  st.subheader("Configurar la modalidad")
