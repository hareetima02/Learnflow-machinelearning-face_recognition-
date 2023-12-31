#IMPORT NECESSARY LIBRARIES 
import streamlit as st
import tensorflow as tf
from tensorflow.keras import models

import numpy as np
import os
import cv2


model = models.load_model('D:\\Hareetima_lf_project\\task1_faceemotion\\face_emotion_recognition.keras')
emotions = [['angry'],
 ['disgust'],
 ['fear'],
 ['happy'],
 ['neutral'],
 ['sad'],
 ['surprise']]

st.text("by HAREETIMA SONKAR")
st.text("Task 1 ")
st.header('Facial Emotion Recognition')
image_path= st.text_input('Enter Image Path')

#image = cv2.imread('image_path')[:,:,0]
#image = cv2.imread('D:\\Hareetima_lf_project\\task1_faceemotion\\goog_images')[:,:,0]
# Read the image
image = cv2.imread(image_path)[:,:,0]

image = cv2.resize(image, (48, 48))
image = np.invert(np.array([image]))

output = np.argmax(model.predict(image))
outcome = emotions[output]
stn = 'Emotion in the Image is '+ str(outcome)
st.markdown(stn)

image_name = os.path.basename(image_path)
st.image('goog_images/' +image_name, width =300)
st.success("successfully completed")