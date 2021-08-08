from django.shortcuts import render
from .forms import ImageForm
import numpy as np
import pandas as pd
import keras
from  keras.preprocessing.image import *
import tensorflow as tf
import os

from PIL import Image as PImage
# Create your views here.

def landing(request):
    return render(request, "DetectionApp/landing.html")

def upload(request):
    if(request.method=="POST"):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            image = img_obj.image.url
            img_title = img_obj.title
            age = img_obj.age
            country = img_obj.country
            email = img_obj.age
            print(os.path.join("D:/Hackathons/XHacks/Brain-Tumor-ML"+image))
            a = predict_class(os.path.join("D:/Hackathons/XHacks/Brain-Tumor-ML"+image))
            return render(request, 'DetectionApp/result.html', {'form': form, 'img_obj':img_obj, 'image': image, 'title':img_title, 'age': age, 'country': country, 'email':email,'BT':a})
        else:
            form = ImageForm()
        return render(request, 'DetectionApp/upload.html', {'form': form})
    else:
        return render(request, "DetectionApp/upload.html")

def aboutus(request):
    return render(request, "DetectionApp/about.html")

def result(request):
    return render(request, "DetectionApp/result.html")

model = keras.models.load_model(os.path.join("D:/Hackathons/XHacks/Brain-Tumor-ML/DetectionApp/"+"model.h5")) #loading our model that we will use to make predictions of emotions
def predict_class(img_path):
    img = load_img(img_path)
    image = img
    newsize = (224, 224)
    image = image.resize(newsize)
    img_array_ = np.array(image)
    img_array_ = np.expand_dims(img_array_, axis=0)
    print(img_array_.shape)
    prediction = (model.predict([img_array_])[0])
    print(prediction)
    if(prediction >= 0.5):
        return 1
    else:
        return 0