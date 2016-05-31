
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import CustomUser
from .forms import NewUserForm, EditUserForm


def index(request):
    users = CustomUser.objects.all()
    return render(request, 'users/index.html', {'users': users})


def new_user(request):

    if request.method == 'GET':
        return render(request, 'users/new.html', {'form': NewUserForm()})

    elif request.method == 'POST':

        form = NewUserForm(request.POST)

        if not form.is_valid():
            return render(request, 'users/new.html', {'form': form})

        CustomUser.objects.create(
            username=form.cleaned_data['username'],
            date_of_birth=form.cleaned_data['date_of_birth'])

        return redirect(reverse('users:index'))


def edit_user(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'GET':

        form = EditUserForm(initial={'date_of_birth': user.date_of_birth})

        return render(request, 'users/edit.html', {'form': form, 'user': user})

    elif request.method == 'POST':

        form = EditUserForm(request.POST)

        if not form.is_valid():
            return render(request, 'users/edit.html',
                          {'form': form, 'user': user})

        user.date_of_birth = form.cleaned_data['date_of_birth']
        user.save()

        return redirect(reverse('users:index'))


def delete_user(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'GET':
        return render(request, 'users/confirm_delete.html', {'user': user})

    elif request.method == 'POST':

        user.delete()
        return redirect(reverse('users:index'))
