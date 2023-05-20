from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')

def sizes(request):
    return render(request,'sizes.html')

def all_items(request):
    items = Item.objects.all()
    return render(request, 'all_items.html', {'items': items})


def create_item(request):
    if request.method == "POST":
        new_item_form = ItemForm(request.POST)
        if new_item_form.is_valid():
            new_item = new_item_form.save()
            return redirect('all_items')
    else:
        new_item_form = ItemForm()

    return render(request, 'create_item.html', {'form': new_item_form})


def view_single_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'view_single_item.html', {'item': item})
   
def view_by_size(request, size):
    size_obj = Size.objects.get(name=size)
    items = Item.objects.filter(size=size_obj)

    return render(request, 'all_items.html', {'items': items, 'size': size})