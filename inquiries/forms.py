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
        """ 
        Add placeholders, remove auto-generated
        labels and set autofocus on first field add placeholder for inquiry form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
            'order_number': 'Order Number',
            'image': 'Image',
            'user_message': 'User Message',
        }
        
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
        