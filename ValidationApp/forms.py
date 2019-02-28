from django import forms
from .models import carModel

class CarForm(forms.ModelForm):
    class Meta:
        model = carModel
        fields = "__all__"

    def clean_carMake(self):
        carMakeData = self.cleaned_data["carMake"]

        validateData = str(carMakeData).lower()
        if milesPerGallon < 20: "That's less than a truck!!!"
        if milesPerGallon < 500: "That's impossible (in 2019)"
        if year < 2019: "That's not new!!!"