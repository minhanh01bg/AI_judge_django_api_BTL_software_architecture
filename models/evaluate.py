# make a prediction for a new image.
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import os
import pandas as pd
# load and prepare the image
def load_image(filename):
    img = load_img(filename, target_size=(224, 224))
    img = img_to_array(img)
    # img = img / 255.0
    img = img.reshape(1,224,224,3)
    # print(img.shape)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img

# load an image and predict the class
def run_example(name):
    # load the image
    img = load_image(f'./media/images/{name}')
    # load model
    model = load_model('./models/model-20230218-153154.h5')
    # predict the class
    result = model.predict(img)
    # print(result[0])
    return result
# # entry point, run the example
# run_example()