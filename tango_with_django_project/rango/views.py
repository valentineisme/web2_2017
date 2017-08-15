from django.shortcuts import render, HttpResponse

def index(request):
	context_dict = {'boldmessage':'eu quero morrer'}
	return render(request, 'rango/index.html', context_dict)
	
def about(request):
	return HttpResponse("ainda quero morrer <br><br> <a href='/rango/'> inicial </a>")
# Create your views here.
