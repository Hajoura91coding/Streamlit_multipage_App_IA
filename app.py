import streamlit as st
from fastbook import *
from fastai.vision.widgets import *
from fastcore.all import *
from PIL import Image
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

st.title("Food analysis")
st.write("A classifier model about good or not good food for health")



class Predict:


    def __init__(self, filename):
        path = Path()
        self.learn_inf = load_learner(path/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_image()
            self.predict()


    def get_image_from_upload(self):
        img = st.file_uploader(label='load an image of your favorite food', type=['png','jpg'])
        if img is not None:
            img = PILImage.create(img)
            return img
        return None

    def display_image(self):
        st.image(self.img.to_thumb(350,350), caption='Uploaded Image')

    def predict(self):

        if st.button('Classify') :
            pred, pred_idx, probs = self.learn_inf.predict(self.img)
            st.write(f'Prediction: {pred} with a probability of : {probs[pred_idx]:.04f}')
        else:
            st.write(f'Click the button to classify')

if __name__=='__main__':
    model = 'export.pkl'
    predictor = Predict(model)
