from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import OrderForm  # Certifique-se de ter um formulário chamado OrderForm
from django.shortcuts import render
from .models import Cliente, Prato, Garcom

class LoginView(AuthLoginView):
    template_name = 'app/login.html'

class LogoutView(AuthLogoutView):
    template_name = 'app/logout.html'

class IndexView(TemplateView):
    template_name = 'app/index.html'

class SubmitOrderView(FormView):
    form_class = OrderForm
    template_name = 'app/order_form.html'
    success_url = '/success/'  # Redireciona para uma URL de sucesso, ajuste conforme necessário

    def form_valid(self, form):
        # Lógica para processar o pedido
        form.save()
        return super().form_valid(form)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redireciona para uma página de sucesso
    else:
        form = OrderForm()
    return render(request, 'app/order_form.html', {'form': form})



def home(request):
    clientes = Cliente.objects.all()
    pratos = Prato.objects.all()
    garcons = Garcom.objects.all()

    return render(request, 'home.html', {
        'clientes': clientes,
        'pratos': pratos,
        'garcons': garcons
    })