"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


import crudapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudapp.views.main, name='main'),
    path('detail/<int:id>',crudapp.views.detail, name='detail'),
    path('create_page/', crudapp.views.create_page, name='create_page'),
    path('create/', crudapp.views.create, name='create'),
    path('update_page/<int:id>/', crudapp.views.update_page, name='update_page'),
    path('update/<int:id>/', crudapp.views.update, name='update'),
    path('delete/<int:id>/', crudapp.views.delete, name='delete'),
    path('increase/<int:id>', crudapp.views.increase, name="increase"),
    path('decrease/<int:id>', crudapp.views.decrease, name="decrease"),
]


