from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [ 'name', 'email', 'phone_number', 'subject', 
                  'order_number', 'user_message'
                ]


    order_number = forms.CharField(
        label='Order Number',
        required=False
    )
    
    phone_number = forms.CharField(
        label='Phone Number',
        required=False
    )
    

    def __init__(self, *args, **kwargs):
        """ Add placeholders to fields """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email Address',
            'phone_number': 'Your Phone Number',
            'subject': 'Subject',
            'user_message': 'Your Message',
        }


class UserReplyForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['user_reply']

    user_reply = forms.CharField(
        label='Reply',
        required=True,
    )