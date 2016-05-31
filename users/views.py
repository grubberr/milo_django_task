
import csv
from django.http import HttpResponse
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

        form.save()
        return redirect(reverse('users:index'))


def edit_user(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'GET':

        form = EditUserForm(instance=user)
        return render(request, 'users/edit.html', {'form': form, 'user': user})

    elif request.method == 'POST':

        form = EditUserForm(request.POST, instance=user)

        if not form.is_valid():
            return render(request, 'users/edit.html',
                          {'form': form, 'user': user})

        form.save()
        return redirect(reverse('users:index'))


def delete_user(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'GET':
        return render(request, 'users/confirm_delete.html', {'user': user})

    elif request.method == 'POST':

        user.delete()
        return redirect(reverse('users:index'))


def download(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)

    fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth')

    for user in CustomUser.objects.all():

        row = []

        for f in fields:
            if f == 'date_of_birth':
                row.append(getattr(user, f).strftime('%Y-%m-%d'))
            else:
                row.append(getattr(user, f))

        writer.writerow(row)

    return response
