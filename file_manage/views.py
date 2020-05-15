from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from file_manage.form import CustomerForm
from file_manage.models import Customer
from django.views.generic import DetailView, UpdateView, DeleteView
from . import form
from collections import OrderedDict
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    customer_list = Customer.objects.order_by('ref')
    cuslist = {'customers':customer_list}
    return render(request, 'file_manage/index.html', context = cuslist)

def new_customer(request):
    customerForm = CustomerForm()
    if request.method == "POST":
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid():
            customerForm.save(commit=True)
            return index(request)
        else:
            print('invalid form')
    return render(request, 'file_manage/new_customer.html',{'customerForm':customerForm})

class customerInfoview(DetailView):
    model = Customer
    template_name = "file_manage/customer_info.html"
    def get_success_url(self):
        return reverse('customer_info', kwargs={'pk': self.object.pk})

class customerEditview(UpdateView):
    model = Customer
    form_class = CustomerForm

class customerRemoveview(DeleteView):
    model = Customer
    success_url = reverse_lazy('index')