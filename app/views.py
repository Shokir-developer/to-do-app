from django.shortcuts import render, redirect
from .models import ToDoApp
from .forms import FormToDo

def homepage(request):
	queryset = ToDoApp.objects.all()

	context = {'events': queryset}
	return render(request, 'app/homepage.html', context)

def createForm(request):
	form = FormToDo()

	if request.method == 'POST':
		form = FormToDo(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}

	return render(request, 'app/form.html', context)

def updateForm(request, pk):
	edit = ToDoApp.objects.get(id=pk)
	form = FormToDo(instance=edit)
	if request.method == 'POST':
		form = FormToDo(request.POST, instance=edit)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'app/form.html', context)

def deleteForm(request, pk):
	edit = ToDoApp.objects.get(id=pk)
	if request.method == 'POST':
		edit.delete()

		return redirect('/')

	context = {'edit':edit}

	return render(request, 'app/delete.html', context)