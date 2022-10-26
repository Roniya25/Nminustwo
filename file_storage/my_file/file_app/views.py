from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_data')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


def list_data(request):
    all_data = Personal.objects.all()
    return render(request, 'list_data.html', {'all_data': all_data})


def search(request):
    if 'searched' in request.GET:
        searched = request.GET['searched']
        data = Q(Q(Name__icontains=searched) | Q(Description__icontains=searched))
        name = Personal.objects.filter(data)
        return render(request, 'search.html', {'searched': searched, 'name': name})
    else:
        return render(request, 'search.html')

