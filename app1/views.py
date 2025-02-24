from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from app1.models import Icecream, Order
from app1.forms import OrderForm

# Create your views here.
def home(request):
    return render(request, "home.html")
    

def flavors(request):
    icecreams = Icecream.objects.all()
    return render(request, "flavors.html", {"icecreams": icecreams})
    

def order_icecream(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            icecream_id = form.cleaned_data['icecream'].id
            number_of_scoops = form.cleaned_data['number_of_scoops']
            icecream = Icecream.objects.get(id=icecream_id)
            order = Order.objects.create(icecream=icecream, number_of_scoops=number_of_scoops)
            return redirect(reverse('order_success', kwargs={'order_id': order.id}))
    else:
        form = OrderForm()

    available_icecreams = Icecream.objects.filter(is_available=True)
    context = {
        'form': form,
        'available_icecreams': available_icecreams,
    }
    return render(request, 'order_icecream.html', context)
    
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'order_success.html', context)