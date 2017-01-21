from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from bootcamp.authentication.forms import SignUpForm
from django.contrib.auth.models import User
from bootcamp.feeds.models import Feed


def signup(request):
    if request.method == 'POST':
        print "******************sighup pos*********"
        print request
        print request.POST
        print SignUpForm(request.POST)#this function error!
        print "@@@@@@@@@@@@@@@@signupform(request.POST)"
        form = SignUpForm(request.POST)# error occurred
        print form
        print "************form********* error eccurred !!!!!!!!!!!!"
        if not form.is_valid():
            print "************error****************"
            print request
            return render(request, 'authentication/signup.html',
                          {'form': form})

        else:
            print "**************username"
            username = form.cleaned_data.get('username')
            print username
            email = form.cleaned_data.get('email')
            print email
            password = form.cleaned_data.get('password')
            print password
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = u'{0} has joined the network.'.format(user.username,
                                                                 user.username)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return redirect('/')

    else:
        return render(request, 'authentication/signup.html',
                      {'form': SignUpForm()})
