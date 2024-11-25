from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Vista para la raíz del sitio
def home(request):
    return HttpResponse("¡Bienvenido a mi aplicación!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', home),  # Aquí agregamos la vista para la URL raíz
]
