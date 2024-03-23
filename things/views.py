from django.shortcuts import render
from things.models import Thing

def thing_index(request):
  things = Thing.objects.all()
  context = {
    'things': things,
  }
  return render(request, 'things/index.html', context)

def thing_detail(request, pk):
  thing = Thing.objects.get(pk=pk)
  context = {
    'thing': thing,
  }
  return render(request, 'things/detail.html', context)