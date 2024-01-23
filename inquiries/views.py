from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Inquiry
from .forms import InquiryForm


@login_required
def submit_inquiry(request):
    """ 
    A view for users to submit Trade In Inquiries 
    or other inquiries and view them 
    """
    inquiries = Inquiry.objects.filter(user=request.user)
    inquiries = inquiries.order_by('-created_on')

    if request.method == 'POST':
        form = InquiryForm(request.POST, request.FILES)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            message_text = 'Your inquiry has been submitted successfully and will be reviewed shortly.'
            messages.success(request, message_text)
            return redirect()    
    else:
        inquiry_form = InquiryForm()

    context = {
        'inquiries': inquiries,
        'inquiry_form': inquiry_form,
    }
    return render(request, context)

