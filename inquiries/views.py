from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Inquiry
from .forms import InquiryForm



@login_required
def user_inquiry(request):
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
            return redirect('inquiries')    
    else:
        form = InquiryForm()

    context = {
        'inquiries': inquiries,
        'form': form,
    }
    return render(request, 'inquiries/inquiries.html', context)

@login_required
def view_inquiry(request, inquiry_id):
    """
    A view to view an inquiry's details
    """

    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)

    return render(request, 'inquiries/view_inquiry.html', {'inquiry': inquiry})    


@login_required
def delete_inquiry(request, inquiry_id):
    """
    A view to delete an inquiry
    """
    inquiry = get_object_or_404(Inquiry, pk=inquiry_id)

    if request.method == 'POST':
        inquiry.delete()
        messages.success(
            request, 'Your inquiry has been deleted successfully.'
        )
        return redirect('inquiries')
    
    context = {
        'inquiry': inquiry
    }

    return render(request, 'inquiries/delete_inquiry.html', context)


