from django.shortcuts import render,redirect
from .models import todo
from .forms import todoForm

# Create your views here.
def view(request):
	mylist = todo.objects.all()
	myForm = todoForm()
	if request.method == 'POST':
		myForm = todoForm(request.POST)
		if myForm.is_valid():
			myForm.save()
			return redirect('view')
	context = {'mylist':mylist ,'form':myForm}

	return render(request, 'todolist/view.html', context)

def list(request,id):
	mylist = todo.objects.get(id=id)
	if request.method == 'POST':
		if request.POST.get('save'):
			for item in mylist.item_set.all():
				item.text = request.POST.get(f'i{item.text}')
				if request.POST.get(f'c{item.id}') == 'clicked':
					item.is_complete = True
				else:
					item.is_complete = False
				item.save()

		elif request.POST.get('addItem'):
			new = request.POST.get('newItem')
			if len(new) > 2:
				mylist.item_set.create(text=new, is_complete=False)
			else:
				print('INVALID')

	return render(request, 'todolist/list.html', {'mylist':mylist})