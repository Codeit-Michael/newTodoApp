from django.shortcuts import render,redirect
from .models import todo
from django.http import HttpResponse
from .forms import todoForm

# Create your views here.
def view(request):
	mylist = todo.objects.all()
	return render(request, 'todolist/view.html', {'mylist':mylist})

def new(request):
	myForm = todoForm()
	if request.method == 'POST':
		myForm = todoForm(request.POST)
		if myForm.is_valid():
			# newlist = myForm.cleaned_data['name']
			# listname = todo(name=newlist)
			# listname.save()
			myForm.save()
			return redirect('view')

	return render(request, 'todolist/new.html', {'form':myForm})