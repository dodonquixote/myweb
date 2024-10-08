from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import ProfilMahasiswaForm
from dashboard.models import BiodataMahasiswa

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    profilmahasiswa = get_object_or_404(ProfilMahasiswa, user=request.user)
    biodatamahasiswa = get_object_or_404(BiodataMahasiswa, user=request.user)
    return render(request, 'profil/profil.html', {'profilmahasiswa': profilmahasiswa, 'biodatamahasiswa': biodatamahasiswa})

@login_required(login_url=settings.LOGIN_URL)
def edit_profil(request):
    profilmahasiswa = get_object_or_404(ProfilMahasiswa, user=request.user)
    biodatamahasiswa = get_object_or_404(BiodataMahasiswa, user=request.user)
    return render(request, 'profil/edit_profil.html', {'profilmahasiswa': profilmahasiswa, 'biodatamahasiswa': biodatamahasiswa})

def updated_profil(request):
    profilmahasiswa = ProfilMahasiswa.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfilMahasiswaForm(request.POST, instance=profilmahasiswa)
        if form.is_valid():
            form.save()
            return redirect('profil')  # Redirect ke halaman profil setelah update
    else:
        form = ProfilMahasiswaForm(instance=profilmahasiswa)

    return render(request, 'profil/edit_profil.html', {'form': form})


