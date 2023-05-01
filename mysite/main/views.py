from django.shortcuts import render, redirect
from .forms import NewUserForm, BookForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import AboutUs, MenuFood, Book, Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('index')
    aboutus = AboutUs.objects.all()[0]
    menufood_list = MenuFood.objects.all()
    form = BookForm()
    contact_list = Contact.objects.all()
    return render(request, 'main/index.html', context={
        'aboutus':aboutus,
        'menufood_list':menufood_list,
	    'form':form,
	    'contact_list':contact_list
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			Contact.objects.create(**form.cleaned_data)
			return redirect('index')
	else:
		form = ContactForm()
	return render(request, 'main/contact.html', context={
		'form':form
    })