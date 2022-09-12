from __future__ import division, print_function
from unittest import result

import numpy as np


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array


labels= {'potato_early_blight':0,"potato_late_blight":1,"potato_healthy":2}
## loading the saved model
model= load_model("potatoes.h5")

def model_predict(new_scr):
    img = load_img(str(new_scr), target_size=(256, 256))
    # plt.imshow(img)
    img = img_to_array(img)
    # img = img / 255
    # print(img, img.shape)

    img = img.reshape(1, 256, 256, 3)
    result = model.predict(img)
    print(result)
    preds1 = np.argmax(result, axis=1)
    print(preds1)
    if preds1==0:
        preds1 = "Early_blight Disease Detected"

    elif preds1==1:
        preds1 = "Late_blight Disease Detected"

    elif preds1==2:
        preds1 = "It is a Healthy leaf"


    return preds1

#     for i in labels:

#         if np.argmax(result) == labels[i]:
#             a=i

# #
#     return()

# from keras import models
# model = models.load_model('model (4).h5')
# def model_predict(new_scr):
#     print(new_scr)
#     img = image.load_img(new_scr, target_size=(256, 256))
#     x = image.img_to_array(img)
#     x = x / 255
#     x = np.expand_dims(x, axis=0)
#     preds = model.predict(x)
#     preds1 = np.argmax(preds, axis=1)
#     if preds1 ==0:
#         preds1 = "The leaf is diseased Potato___Early_blight"
#     elif preds1 ==1:
#         preds1 = "The leaf is diseased Potato___late_blight"
#     elif preds1 ==2:
#         preds1 = "The leaf is diseased Potato___healthy"

#     return preds1



