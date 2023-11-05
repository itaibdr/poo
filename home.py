import streamlit as st
import pymongo
from PIL import Image
import numpy as np
import pickle5 as pickle
from bson.binary import Binary
st.balloons()
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(st.secrets["str"])

client = init_connection().test

cons = st.text_input('enter consistency')
img = st.camera_input('take a pic 💩💩')

if (img is not None) and (cons is not None):
    # To read image file buffer as a PIL Image:
    img = Image.open(img)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)
    client.poo.insert_one({'img':Binary(pickle.dumps(img_array, protocol=2), subtype=128),'consistency':cons})
    st.write("## Poo stored!!!")
    st.balloons()
    cons = None
    img = None





