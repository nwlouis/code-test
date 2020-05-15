from django import forms
from django.forms import modelformset_factory
from file_manage.models import Customer
from code_test import settings
from crispy_forms.helper import FormHelper

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name', 'date_of_birth','ref']