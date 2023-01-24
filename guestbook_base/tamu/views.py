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
    edit_tamu = Tamu.objects.get(id==id)
    return render(request, 'edit.html', {'edit_tamu':edit_tamu})

def update(request, id):
    update_tamu = Tamu.Objecs.get(id==id)
    form = FormTamu(request.POST, instance = update_tamu)
    
    if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    return render(request, 'edit.html', {'update_tamu':update_tamu})
    
def delete(request, id):
    delete_tamu = Tamu.Objects.get(id==id)
    delete_tamu.delete()
    return redirect('/show')