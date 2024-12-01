from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Cek tipe user dan redirect ke dashboard yang sesuai
            if user.is_admin:
                return redirect('dashboard_admin')
            elif user.is_staff:
                return redirect('dashboard_staff')
            elif user.is_pelanggan:
                return redirect('dashboard_pelanggan')
            else:
                return redirect('home')  # Default redirect jika tipe user tidak sesuai
        else:
            messages.error(request, 'Username atau password salah')
    
    return render (request, 'accounts/login.html')


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_pelanggan = models.BooleanField('Is pelanggan', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    # Field baru
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
