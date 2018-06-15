from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context = context_dict)
	#return HttpResponse(
	#	"Rango says hello pals! <br/> <a href='/rango/about'>About</a>")

def about(request):
	#return HttpResponse(
	#	"Rango says what about me? <br/> <a href='/rango/index'>Index</a>")
	return render(request, 'rango/about.html')
