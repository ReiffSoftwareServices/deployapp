from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from django.contrib.auth.decorators import login_required


#### import forms
from .forms import *
from django.http import HttpResponseRedirect

## This stuff taken from the project level!

@login_required(login_url= '/accounts/login')
def index(request):
	return render(request, 'interface/index.php', {'wert': 'Eigener Text'})


def design(request):
	return render(request, 'interface/index.php', {'wert': 'Eigener Text'})


# https://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django

class registration(TemplateView):
	template_name= 'registration/register.html'

	def user_registration(self, request):
		form= UserRegistrationForm(request.POST)
		if request.method== 'POST':  #If data was posted
			if form.is_valid():
				first_name= form.cleaned_data['first_name']
				last_name= form.cleand_data['last_name']
				email= form.cleand_data['email']
				username= form.cleand_data['username']
				password= form.cleand_data['password']
				return HttpResponseRedirect('/home/')  #https://docs.djangoproject.com/en/dev/topics/forms/#using-a-form-in-a-view
		#
			else:
				 form= UserRegistrationForm()
		#
		return render(request, self.template_name, {'form': form})

#new_user= User.objects.create_user









# class IndexView(TemplateView):
#     template_name= 'index.php'
#
#
#     @login_required()    # https://docs.djangoproject.com/en/2.0/topics/auth/default/
#     def view_index(self, request):
#         return render(request, self.template_name)
