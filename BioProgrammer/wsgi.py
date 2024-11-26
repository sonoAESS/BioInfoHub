"""
WSGI config for djangoCRUD project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BioProgrammer.settings')

# Inicializa la aplicación WSGI
application = get_wsgi_application()

def create_superuser():
    User = get_user_model()
    username = 'aess' 
    email = 'eliasyosoto@gmail.com'  
    password = 'aesspassword' 
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuario creado exitosamente.")
    else:
        print("El superusuario ya existe.")

create_superuser()