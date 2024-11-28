from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app_base.urls")),
    path('', include("hospital_app.urls")),
    path('medico_app/', include('medico_app.urls')),
]
