from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        usernm = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=usernm, password=p)
        if not user:
            messages.info(request, "Invalid Credentials")
            return redirect("/travello/accounts/login")
        else:
            auth.login(request, user)
            print("Logged in")
            return redirect('/travello')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/travello")


def register(request):
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        user = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']

        if p1 == p2:
            if User.objects.filter(username=user).exists():
                print("User already taken..")
                messages.info(request, "User name already taken..")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email already taken..")
                messages.info(request, "Email already taken..")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user, password=p1, email=email, first_name=f, last_name=l)
                print("User Created")
                user.save()
                return redirect('/travello/accounts/login')
        else:
            print("Password does not match....")
            messages.info(request, "Password doen not match..")
            return redirect('register')
    else:
        return render(request, 'register.html')


