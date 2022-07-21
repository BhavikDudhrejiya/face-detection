import imp
import streamlit as st
import cv2
from PIL import Image
from func import *

st.title('Face Attributes Detections')

image_input = st.file_uploader('Upload image:')

if image_input is not None:
    with open('temp.jpg','wb') as f:
        f.write(image_input.read())

# face_part = detect_face_part('temp.jpg')
# image_box = get_face_box('temp.jpg', face_part)

emotion = detect_emotion('temp.jpg')
age = detect_age('temp.jpg')
gender = detect_gender('temp.jpg')
race = detect_race('temp.jpg')

if st.button('Detect'):
    st.write('''---''')
    st.subheader('Attributes:')
    c1, c2 = st.columns(2)
    image = Image.open('temp.jpg')
    c1.image(image)

    # image2 = Image.open('temp2.jpg')
    # c2.image(image2)
    c2.write(f'Age:`{age}`')
    c2.write(f'Gender: `{gender}`')
    c2.write(f'Emotions: `{emotion}`')
    c2.write(f'Race: `{race}`')

  


