from django.http import HttpResponse

def index(request):
	return HttpResponse("Was geht ab? Es klappt")