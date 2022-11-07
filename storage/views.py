from django.db.models import Sum
from django.shortcuts import render

from storage.models import Order, Position


def index(request):
    complite = Order.objects.values('pk').filter(status='готово').count()
    income = Order.objects.values('pk').filter(status='принято').count()
    count = 0
    pos = Position.objects.values('quantity').filter(order__status='готово')
    for q in pos:
        count += q['quantity']
    pos = Position.objects.values('quantity').filter(order__status='принято')
    for q in pos:
        count += q['quantity']
    context = {
        'complite': complite,
        'income': income,
        'count': count
    }
    return render(request, 'home.html', context)


def workshop(request):
    orders_c = Order.objects.filter(status='готово')
    context = {
        'orders_c': orders_c
    }
    return render(request, 'workshop.html', context)
