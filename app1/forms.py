# forms.py
from django import forms
from .models import Order

#  inherits from Django's ModelForm class
class OrderForm(forms.ModelForm): 
    
    # The inner Meta class is a required component of a ModelForm.
    #  used to provide metadata for the OrderForm class.
    class Meta:
        # Django will  automatically generate form fields
        #based on the fields defined in the Order model.
        model = Order  
        # specifies the fields from the Order model that should be included in the form
        fields = ['icecream', 'number_of_scoops']