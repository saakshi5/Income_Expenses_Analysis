from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'expenses/index.html')

def add_expense(request):
    return render(request,'expenses/add_expense.html')

def income(request):
    return render(request,'income/index.html')

def stats(request):
    return render(request,'expenses/stats.html')

def preferences(request):
    return render(request,'expenses/index.html')