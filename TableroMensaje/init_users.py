import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TableroMensaje.settings')


from django.contrib.auth.models import User

def init_users():
    user1 = User.objects.create_user(username='usuario1', password='1221')
    
    user2 = User.objects.create_user(username='usuario2', password='2112')

    print("Usuarios creados exitosamente.")

if __name__ == '__main__':
    init_users()
