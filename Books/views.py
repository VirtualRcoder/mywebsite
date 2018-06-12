from django.shortcuts import render,HttpResponse
from django.template import loader
from Books.models import Book
from Books.forms import ContactForm
from django.core.mail import send_mail, get_connection
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def hello(request):
	h='<html><body><h1>MY NAME IS VIRTUALRCODER</h1>%s</body></html>'
	ua=request.META.get('HTTP_USER_AGENT', 'unknown')
	return HttpResponse(h%ua)

def Login(request):
	return render(request,'Books/Login.html')

def Register(request):
	return render(request,'Books/Register.html')

def Home(request):
	return render(request,'Books/Home.html')	

def About(request):
	return render(request,'Books/About.html')

def Contact(request):
	return render(request,'Books/Contact.html')

def search_form(request):
    return render(request, 'Books/search_form.html')	

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'Books/search_results.html', {'Books': books, 'query': q})
    return render(request, 'Books/search_form.html', {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
        
    return render(request, 'Books/contact_form.html', {'form':form})