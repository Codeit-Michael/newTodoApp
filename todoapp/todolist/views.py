from django.shortcuts import render,redirect
from .models import todo
from .forms import todoForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
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

 
@login_required(login_url='login')
def list(request,id):
	mylist = todo.objects.get(id=id)
	if request.method == 'POST':
		if request.POST.get('save'):
			for item in mylist.item_set.all():
				if item.text != request.POST.get(f'i{item.text}'):
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

		elif request.POST.get('delThis'):
			item_index = request.POST.get('delThis')
			mylist.item_set.get(id=item_index).delete()

	context = {'mylist':mylist}

	return render(request, 'todolist/list.html', context)


def signup(request):
	if request.user.is_authenticated:
		return redirect('view')

	else:
		user_form = CreateUserForm()
		if request.method == 'POST':
			user_form = CreateUserForm(request.POST)
			if user_form.is_valid():
				user_form.save()
				user_name = user_form.cleaned_data.get('username')
				messages.success(request,f'user "{user_name}" is successfully created!!')
				return redirect('login')

		context = {'form':user_form}

	return render(request, 'todolist/signup.html', context)


def signin(request):
	if request.user.is_authenticated:
		return redirect('view')

	else:
		if request.method == 'POST':
			name = request.POST.get('name')
			password = request.POST.get('pass') 
			user = authenticate(request, username=name, password=password)
			if user is not None:
				login(request,user)
				return redirect('view')

	return render(request, 'todolist/signin.html')


def signout(request):
	logout(request)
	messages.success(request, 'User successfully logged out')
	return redirect('signin')


def deleteList(request):
	mylist = request.GET.get('delThis')
	deletelist = todo.objects.get(id=int(mylist)).delete()
	return redirect('view')
