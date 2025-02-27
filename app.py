import streamlit as st
from PIL import Image

st.title(" Mi primera cosa")

st.header("Una caraca re chida.")
st.write("Si que estamos chida!!!")
image = Image.open("armydark5.jpg")

st.image(image, caption="Interfaces multimodales")
