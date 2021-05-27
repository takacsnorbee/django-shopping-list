from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('21232f297a57a5a743894a0e4a801fc3/', admin.site.urls),
    path('', include('shopping_list.urls'))
]
