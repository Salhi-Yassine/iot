# from django.shortcuts import render
import csv
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Temperature


def home(request):
    return HttpResponse('hello')


def dht(request):
    tab = Temperature.objects.all()
    # print(tab)
    s = {'tab': tab}
    return render(request, 'tables.html', s)


class EditorChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = Temperature.objects.all()
        return context


def exp_csv(request):
    obj = Temperature.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])
    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def temperature(request):
    tab = Temperature.objects.latest('dt')
    # print(tab)
    s = {'last': tab}
    return render(request, 'last.html', s)
