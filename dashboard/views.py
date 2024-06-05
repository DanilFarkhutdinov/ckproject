from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import AnnualSalary, Difference
from django.core import serializers


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = AnnualSalary.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def dashboard_inflation(request):
    return render(request, 'dashboard_inflation.html', {})


def inflation_data(request):
    dataset = Difference.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
