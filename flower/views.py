from django.shortcuts import render, get_object_or_404

# Create your views here.
from flower.models import Flower
from django.http import HttpResponseRedirect
from login.forms import FlowerForm

from django.contrib.auth.decorators import permission_required

@permission_required('flower.add_flower')
def create(request):
    if request.method == "POST":
        form = FlowerForm(request.POST, request.FILES) # 加上request.FILES才能存圖片
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = FlowerForm()
    return render(request, "flower/edit.html", {'form': form})

@permission_required('flower.change_flower')
def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = FlowerForm(request.POST, request.FILES, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = FlowerForm(instance=flower)
    return render(request, "flower/edit.html", {'form': form})

@permission_required('flower.delete_flower')
def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return HttpResponseRedirect("/")


def flower(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q == "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    
    return render(request, 'flower/flower.html', {'flowers': flowers })

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', {'flower': flower})

def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'flower/flower.html', {'flowers': flowers})