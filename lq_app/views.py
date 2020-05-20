from django.shortcuts import render

from lq_app.forms import UserForm, LaundrerForm, CustomerForm, LoadForm
from django.urls import reverse
from lq_app.models import  Customer, Laundrer, Load, Order
from lq_app.decorators import customer_required, laundrer_required

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required


# Create your views here.

def landing(request):
    return render(request,'lq_app/landing.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('landing'))

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        return HttpResponse(user)


        if user:

            if user.laundrer:

                login(request,user)

                return HttpResponseRedirect(reverse('lq_app:laundrer_landing'))

            elif user.is_customer:
                login(request,user)

                return HttpResponseRedirect(reverse('lq_app:customer_landing'))
            else:

                return HttpResponseRedirect("lq_app/landing")
        else:

            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'lq_app/login.html', {})


#laundrer_landing

#laundrer_login

#laundrer_register

#customer_landing

#customer_login
def customer_register(request):
    form = UserForm(request.POST)
    customer_form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request,'lq_app/customer_register.html')

def Laundrer_register(request):
    form = UserForm(request.POST)
    laundrer_form = LaundrerForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request,'lq_app/customer_register.html')

#customer_register

class LoadsListView(ListView):
    model = Load
    def get_queryset(self):
        return Load.objects.filter(date=timezone.now()).order_by('date')

class LoadCompleteView(LoginRequiredMixin,DeleteView):
    model = Load
    success_url = reverse_lazy('load_complete')
    def get_queryset(self):
        return Load.objects.filter(customer = user, date=timezone.now()).order_by('date')

class CreateLoadView(LoginRequiredMixin,CreateView):
    login_url = '/create/'
    redirect_field_name = '/landing.html'
    form_class = PostLoad
    model = Load
