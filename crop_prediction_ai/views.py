from django.shortcuts import render
from django.http import HttpResponse
from .forms import CropPredictionForm
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from keras.utils import to_categorical
def home(request):
	return render(request, 'home.html', { None:None })
def predictcrop(request):
	if request.method=='GET':
		return render(request, 'predictcrop.html', {'form':CropPredictionForm})
	elif request.method=='POST':
		try:
			crops = pd.read_csv(staticfiles_storage.path(settings.STATIC_ROOT / 'crops.csv'))
			encode_dic = {'label':{'rice': 1,'maize': 2,'chickpea': 3,'kidneybeans': 4,'pigeonpeas': 5,'mothbeans': 6,'blackgram': 7,'lentil': 8,'banana': 9,'mango': 10,'watermelon': 11,'apple': 12,'orange': 13,'papaya': 14,'coconut': 15,'cotton': 16,'jute': 17,'coffee': 18,'mungbean':19,'pomegranate':20,'grapes':21,'muskmelon':22}}
			crops = crops.replace(encode_dic)
			x_values = crops[['N','P','K','temperature','humidity','ph','rainfall']]
			x_valuesdf = pd.DataFrame(x_values)
			y_values = crops['label']
			y_values
			y_values = to_categorical(y_values)
			ai = Sequential()
			ai.add(Dense(20, input_dim=7, activation='relu'))
			ai.add(Dense(20, activation='relu'))
			ai.add(Dense(20, activation='relu'))
			ai.add(Dense(20, activation='relu'))
			ai.add(Dense(23, activation='softmax'))
			ai.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
			ai.fit(x_valuesdf, y_values, epochs=20, shuffle=True)
			# x_values = crops[['N','P','K','temperature','humidity','ph','rainfall']]
			# x_valuesdf = pd.DataFrame(x_values)
			# y_values = crops['label']
			# y_values
			# y_values = to_categorical(y_values)
			# ai = Sequential()
			# ai.add(Dense(20, input_dim=7, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(20, activation='relu'))
			# ai.add(Dense(23, activation='softmax'))
			# ai.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
			# ai.fit(x_valuesdf, y_values, epochs=20, shuffle=True)
			test = pd.DataFrame()
			test['N']=[int(request.POST.get('Nitrogen_in_soil'))]
			test['P']=[int(request.POST.get('Phosphorus_in_soil'))]
			test['K']=[int(request.POST.get('Pottasium_in_soil'))]
			test['temperature']=[int(request.POST.get('temperature'))]
			test['rainfall']=[int(request.POST.get('rainfall_in_mm'))]
			test['ph']=[int(request.POST.get('Soil_ph_value'))]
			test['humidity']=[int(request.POST.get('humidity'))]
			test.info()
			crop_type = ai.predict(test)
			crop_type = np.argmax(crop_type)
			crop_type = list(encode_dic.get('label').keys())[list(encode_dic.get('label').values()).index(crop_type)]
			return render(request, 'predictcrop.html', {'form':CropPredictionForm, 'crop':crop_type})
		except ValueError:
			return render(request, 'predictcrop.html', {'form':CropPredictionForm, 'error_value_name_type':"All fields should have a number error type: TypeError"})