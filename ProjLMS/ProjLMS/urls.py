from django.contrib import admin
from django.urls import path
from disciplina.views import *

urlpatterns = [
	path('',index),
	path('',disciplina),
	path('',professor),
    path('admin/', admin.site.urls),
]
