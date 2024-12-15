from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Create your views here.
def sign_up_by_django(request):
    users = ['login1', 'user1', 'admin']
    info = {'form': UserRegister()}

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) < 18:
                    info['error'] = 'Вам должно быть больше 18 лет'
                elif username in users:
                    info['error'] = 'Такой пользователь уже существует'
        else:
            info['form'] = form 

    return render(request, 'fifth_task/registration_page.html', {'info': info}) 


def sign_up_by_html(request):
    users = ['login1', 'user1', 'admin']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
        elif username in users:
            info['error'] = 'Такой пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', {'info': info})
