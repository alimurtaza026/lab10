from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View, ListView
from .forms import UserDataForm, ShippingDataform
from .models import UserDataModel, ShippindDataModel


class UserDataFormView(View):
    def get(self, *args, **kwargs):
        form = UserDataForm()
        context = {
            'form': form
        }
        return render(self.request, 'userdataform.html', context)

    def post(self, *args, **kwargs):
        print(self.request.POST['first_name'])

        first_name = self.request.POST['first_name']
        last_name = self.request.POST['last_name']

        email = self.request.POST['email']
        print(email)
        UserDataModel.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)

        return redirect('core:userdatalist')


class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'homepage.html')


class UserDataListView(ListView):
    model = UserDataModel
    template_name = 'userdatadetailspage.html'


class ShippingDataFormView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'ShippingDataForm.html')

    def post(self, *args, **kwargs):

        first_name = self.request.POST['receiver_first_name']
        last_name = self.request.POST['receiver_last_name']

        email = self.request.POST['receiver_address']
        ShippindDataModel.objects.get_or_create(receiver_first_name=first_name, receiver_last_name=last_name, receiver_address=email)

        return redirect('core:shippingdatalist')
class ShippingDataListView(ListView):
    model = ShippindDataModel
    template_name = 'shippingdetailspage.html'
