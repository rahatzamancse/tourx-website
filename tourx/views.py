from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic.base import View
from tourx.forms import UserForm


class UserFormView(View):
    form_class = UserForm

    # template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print('done')

        if form.is_valid():
            print('done')
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            print(user)
            user.save()

            user = authenticate(username=username, password=password)

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
