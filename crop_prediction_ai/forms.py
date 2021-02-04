from django.db import models
from django import forms

class CropPredictor(models.Model):
	Nitrogen_in_soil = models.IntegerField()
	Phosphorus_in_soil = models.IntegerField()
	Pottasium_in_soil = models.IntegerField()
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	Soil_ph_value = models.IntegerField()
	rainfall_in_mm = models.IntegerField()
class CropPredictionForm(forms.ModelForm):
	class Meta():
		model = CropPredictor
		fields = ['Nitrogen_in_soil', 'Phosphorus_in_soil', 'Pottasium_in_soil', 'temperature', 'humidity', 'Soil_ph_value', 'rainfall_in_mm']
		widgets = {
		'Nitrogen_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Phosphorus_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Pottasium_in_soil':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'temperature':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'humidity':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'rainfall_in_mm':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"}),
		'Soil_ph_value':forms.TextInput(attrs={'class':"form-control", 'id':"floatingInput"})
	}
