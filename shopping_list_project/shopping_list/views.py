from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError, models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Shopping_list
from django.contrib.auth.decorators import login_required
from json import dumps

def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method =='GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', { 'error': 'Username or password dont match'})
        else:
            login(request, user)
            return redirect('shoppinglist')


def logout_user(request):
    logout(request)
    return redirect('home')


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('shoppinglist')
            except IntegrityError:
                return render(request, 'signup.html', {'error': 'Name already taken'})
        else:
            return render(request, 'signup.html', { 'error' : 'Passwords dont match'})

@login_required
def shoppinglist(request):
    if request.method == 'POST':
        list_id = request.POST['deleteThisList']
        Shopping_list.objects.filter(id=list_id).delete()
        updated_user_lists = Shopping_list.objects.all().filter(user_id=request.user.id)
        return render(request, 'shoppinglist.html', {'lists':updated_user_lists})
    else:
        user_lists = Shopping_list.objects.all().filter(user_id=request.user.id)
        return render(request, 'shoppinglist.html', {'lists':user_lists})
    

@login_required
def addlist(request):
    if request.method == 'GET':
        return render(request, 'addnewlist.html')
    else:
        new_list_name = request.POST['listname']
        new_list_elements = request.POST['saveThisListToBackend']
        new_list = Shopping_list(list_name=new_list_name, list_items=new_list_elements, user=request.user)
        new_list.save()
        return redirect('shoppinglist')
        

@login_required
def shoppinglistitems(request, list_id):

    if request.method == 'POST':
        updated_data_from_frontend = request.POST['updatedList'].replace(';', '').replace(',', ';')
        temp_list_object = get_object_or_404(Shopping_list, pk=list_id, user=request.user)
        temp_list_object.list_items = updated_data_from_frontend
        temp_list_object.save()
        return redirect('shoppinglist')
    else:    
        list_item = get_object_or_404(Shopping_list, pk=list_id, user=request.user).list_items.split(';')
        cleared_list = list(set([i.strip() for i in list_item]))
        
        for ele in cleared_list:
            if len(ele) == 0:
                cleared_list.remove(ele)
        
        json_to_frontend = dumps({0: cleared_list})
        return render(request, 'viewlistitems.html', {'list': json_to_frontend})
