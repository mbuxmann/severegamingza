from django.shortcuts import render, redirect
from . forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('pages:home')
            
    
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form':form})