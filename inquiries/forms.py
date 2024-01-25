from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [ 'name', 'email', 'phone_number', 'subject', 
                  'order_number', 'image', 'user_message'
                ]
    
    phone_number = forms.CharField(
        label='Phone Number',
        required=False
    )

    order_number = forms.CharField(
        label='Order Number',
        required=False
    )

    image = forms.ImageField(
        label='Image',
        required=False
    )
    

    def __init__(self, *args, **kwargs):
        """ Add placeholders to fields """
        super().__init__(*args, **kwargs)
