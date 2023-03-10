from django.shortcuts import render, redirect
from tamu.forms import FormTamu
from tamu.models import Tamu

# Create your views here.
def reqtamu(request):
    if request.method == "POST":
        form = FormTamu(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = FormTamu()
    return render(request, 'index.html', {'form':form})
    
def show(request):
    show_tamu = Tamu.objects.all()
    return render(request, 'show.html', {'show_tamu':show_tamu})

def edit(request, id):
    tamu = Tamu.objects.get(id=id)
    return render(request, 'edit.html', {'tamu':tamu})

def update(request, id):
    tamu = Tamu.objects.get(id=id)
    form = FormTamu(request.POST, instance = tamu)
    
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'tamu':tamu})
    
def delete(request, id):
    tamu = Tamu.objects.get(id=id)
    tamu.delete()
    return redirect('/show')