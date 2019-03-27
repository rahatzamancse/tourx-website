from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template import Context
from django.views.generic import DetailView
from django.views.generic.base import View

from tourx import models
from tourx.forms import ProfileForm


class ProfileFormView(View):
    form_class = ProfileForm

    # template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print('done')

        if form.is_valid():
            print('done')
            profile = form.save(commit=False)
            # profile = Profile.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'], email=form.cleaned_data['email'])
            # profile = form.save(commit=False)
            # profile.user = user
            # profile.save()

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # profile.username = username
            profile.set_password(password)
            # print(user)
            # user.save()
            # profile.user = user
            profile.save()

            user = authenticate(username=email, password=password)

            if user is not None:
                print('done')
                if user.is_active:
                    print('done')
                    login(request, user)
                    print('Successfully created User account')
                    return redirect('wait')

        else:
            return render(request, 'signup.html', {'form': form})


class LoggedinView(View):
    def get(self, request):
        # Here is home
        return render(request, template_name='registration/loggedin.html', context=None)

    def post(self, request):
        return render(request, template_name='registration/loggedin.html', context=None)


def tour(request, val):
    print('In tour')
    if val == '1':
        jumbo_title = 'I want to travel to...'
        search = 'Sylhet?'
        next_des = 2
        typ = 'tour'
        context = {'jumbo_title': jumbo_title, 'search': search, 'next': next_des, 'type': typ}
        return render(request, template_name='tour.html', context=context)
    elif val == '2':
        jumbo_title = 'I want to go by...'
        search = '4 wheel tempo'
        next_des = 3
        typ = 'tour'
        context = {'jumbo_title': jumbo_title, 'search': search, 'next': next_des, 'type': typ}
        return render(request, template_name='tour.html', context=context)
    else:
        product_list = models.Place.objects.all()
        typ = 'tour'
        context = {'products': product_list, 'type': typ}
        print(product_list)
        return render(request, template_name='selection.html', context=context)


def hotel(request, val):
    print('In hotel')
    if val == '1':
        jumbo_title = 'I want to live at...'
        search = 'Sylhet?'
        next_des = 2
        typ = 'hotel'
        context = {'jumbo_title': jumbo_title, 'search': search, 'next': next_des, 'type': typ}
        return render(request, template_name='tour.html', context=context)
    elif val == '2':
        jumbo_title = 'We want to stay for ...'
        search = '4 days'
        next_des = 3
        typ = 'hotel'
        context = {'jumbo_title': jumbo_title, 'search': search, 'next': next_des, 'type': typ}
        return render(request, template_name='tour.html', context=context)
    else:
        product_list = models.Hotel.objects.all()
        typ = 'hotel'
        context = {'products': product_list, 'type': typ}
        print(product_list)
        return render(request, template_name='selection.html', context=context)

