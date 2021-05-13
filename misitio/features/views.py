from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.contrib.postgres.operations import UnaccentExtension, TrigramExtension
from django.contrib import messages
from .models import *





# Create your views here.
def view_list(request):
    current_user = request.user.id
    personal = Todo.objects.filter(user_id=current_user)
    public = Todo.objects.exclude(user_id=current_user)
    return render(request, 'todo_list.html', {'personal': personal, 'public': public})

def add(request):
    if request.method=='POST':
        do = request.POST['todo']
        private = request.POST.get('privacy',False)
        if private=='on':
            private = True
        current_user = request.user.id
        to_do = Todo.objects.create(user_id=current_user, do=do, privacy=private)
        to_do.save()
        messages.success(request, 'To do added successfully')
        return redirect('/list')
    elif request.method!='POST':
        messages.info(request, 'Filler message')
        return redirect('/')
    else:
        messages.error(request, 'To do added unsuccessfully')
        return redirect('/')

def delete(request, todo_id):
    if request.method=="POST":
        todo_delete = Todo.objects.get(id=todo_id)
        todo_delete.delete()
        messages.success(request, 'To do successfully deleted')
    else:
        messages.success(request, 'An unexpected error has occurred')
    
    return redirect('/list')

def grid_view(request):
    grid_list = Grid.objects.all()
    return render(request, 'grid_list.html', {'grid': grid_list, 'edit': False, 'to_edit': None, 'sorting': 'None'})
    
def add_grid(request):
    if request.method=="POST":
        product = request.POST['product']
        price = request.POST['price']
        link = request.POST['link']
        current_user = request.user.id

        grid = Grid.objects.create(user_id=current_user, product=product, price=price, link=link)
        grid.save()
        messages.success(request, 'Grid added successfully')
        return redirect('/grid_list')

    else:
        messages.error(request, 'An unexpected error has occurred')
        return redirect('/')

def delete_grid(request, grid_id):
    if request.method=="POST":
        current_user = request.user.id
        to_delete = Grid.objects.get(id=grid_id)
        grid_user_id = to_delete.user_id
        if current_user==grid_user_id:
            to_delete.delete()
            messages.success(request, 'Grid deleted successfully')
        else:
            messages.warning(request, 'You do not have permission')

    else:
        messages.error(request, 'An unexpected error has ocurred')
        
    return redirect('/grid_list')

def predit_grid(request, grid_id, element):
    if request.method=="POST":
        grid_list = Grid.objects.all()
        edit = True
        to_edit = [grid_id, element]
        return render(request, 'grid_list.html', {'grid': grid_list, 'edit': edit, 'to_edit': to_edit, 'sorting': 'None'})

def edit_grid(request, grid_id, element):
    if request.method=="POST":
        current_user = request.user.id
        new_edit = request.POST['edit']
        to_modify = Grid.objects.get(id=grid_id)
        if element==1:
            to_modify.product = new_edit
            to_modify.save()
            messages.success(request, 'Field modified successfully')
        elif element==2:
            to_modify.price = new_edit
            to_modify.save()
            messages.success(request, 'Field modified successfully')
        elif element==3:
            to_modify.link = new_edit
            to_modify.save()
            messages.success(request, 'Field modified successfully')
        else:
            messages.error(request, 'An unexpected error ocurred')
        
    else:
        messages.warning(request, 'Illegal action')

    return redirect('/grid_list')

from itertools import chain
def search(request):
    to_search = request.GET['word']
    searched1 = Grid.objects.filter(product__trigram_similar=to_search)
    searched2 = Grid.objects.filter(price__trigram_similar=to_search)
    searched = sorted(chain(searched1, searched2), key=lambda instance:instance.product)

    return render(request, 'grid_list.html', {'grid': searched, 'edit': False, 'to_edit': None, 'sorting': 'None'})

def sort(request, element, sorting):
    if request.method=="POST":
        if element == 'product':
            if sorting == 'ascendant':
                grid_list = Grid.objects.order_by('product')
            elif sorting == 'descendant':
                grid_list = Grid.objects.order_by('-product')
        elif element == 'price':
            if sorting == 'ascendant':
                grid_list = Grid.objects.order_by('price')
            elif sorting == 'descendant':
                grid_list = Grid.objects.order_by('-price')
        elif element == 'link':
            if sorting == 'ascendant':
                grid_list = Grid.objects.order_by('link')
            elif sorting == 'descendant':
                grid_list = Grid.objects.order_by('-link')
        else:
            messages.error(request, 'Unexpected error ocurred')
    else:
        grid_list = Grid.objects.all()
        messages.error(request, 'Illegal action')
    
    return render(request, 'grid_list.html', {'grid': grid_list, 'edit': False, 'to_edit': None, 'sorting': sorting})

def error404(request, exception):
    return render(request, '404.html')