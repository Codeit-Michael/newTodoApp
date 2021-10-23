from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# for the decorator we made
from .decorators import unauthenticated_user

# Create your views here.
@login_required(login_url='signin')
def view(request):
	mylist = User.objects.get(username=request.user)
	myForm = TodoForm()
	myForm.user = request.user
	if request.method == 'POST':
		newTodo = mylist.todo_set.create(title=request.POST.get('newItem'))
		return redirect('view')

	context = {'mylist':mylist ,'form':myForm}

	return render(request, 'todolist/view.html', context)


@login_required(login_url='signin')
def list(request,id):
	account = User.objects.get(username=request.user)
	mylist = account.todo_set.get(id=id)
	if request.method == 'POST':
		if request.POST.get('save'):
			for item in mylist.item_set.all():
				if request.POST.get(f'c{item.id}') == 'clicked':
					item.is_complete = True
				else:
					item.is_complete = False
				item.save()
		elif request.POST.get('addItem'):
			new = request.POST.get('newItem')
			mylist.item_set.create(text=new, is_complete=False)
		elif request.POST.get('delThis'):
			item_index = request.POST.get('delThis')
			mylist.item_set.get(id=item_index).delete()

	context = {'mylist':mylist}

	return render(request, 'todolist/list.html', context)


@unauthenticated_user
def signup(request):
	user_form = CreateUserForm()
	if request.method == 'POST':
		user_form = CreateUserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			user_name = user_form.cleaned_data.get('username')
			messages.success(request,f'user "{user_name}" is successfully created!!')
			return redirect('signin')
		else:
			messages.error(request, """Action Denied.. 
				Maybe your Username has space/s or your passwords doesn't 
				match each other""")
			return redirect('signup')

	context = {'form':user_form}

	return render(request, 'todolist/signup.html', context)


@unauthenticated_user
def signin(request):
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
	deletelist = Todo.objects.get(id=int(mylist)).delete()
	return redirect('view')
