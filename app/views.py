from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from .forms import personaForm
from .models import Persona

# Create your views here.
def home(request):
    form=personaForm()
    registro=Persona.objects.all()
    
    return render(request,'base.html',{
        'title':'Home',
        'registros':registro,
        'form':form,
        })

@never_cache
def insertarData(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
               form.save()
               return redirect ('home')
    else:
        form = personaForm()
    
    return render(request, 'insert.html', {'title': 'Home', 'form': form, 'button':'Crear'})

def updateData(request, id):
    registro = Persona.objects.get(pk=id)

    if request.method == 'POST':
        form = personaForm(request.POST, instance=registro)
        if form.is_valid():
            registro.pk=id
            registro.nombre=form.cleaned_data['nombre']
            registro.apellido=form.cleaned_data['apellido']
            registro.telefono=form.cleaned_data['telefono']
            registro.correo=form.cleaned_data['correo']
            
            registro.save()
            return redirect('home')
    else:
        form = personaForm(instance=registro)

    return render(request, 'update.html', {'form': form,'button':'Actualizar'})

def deleteData(request, id):
    regis=Persona.objects.get(id=id)
    regis.delete()
    return redirect ('home')

