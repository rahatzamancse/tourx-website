from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View

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
