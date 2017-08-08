from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("Oi, quero morrer!!!!!! <br><br><br> <a href='/rango/about/'> sobre </a>")
	
def about(request):
	return HttpResponse("ainda quero morrer <br><br> <a href='/rango/'> inicial </a>")
# Create your views here.
