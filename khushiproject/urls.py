"""khushiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views, switch1, switch2, switch3, switch4, switch5, plug1, plug2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('dashboard', views.dashboard, name="index"),
    path('toggle_plug1', plug1.toggle_plug1),
    path('refresh_plug1', plug1.refresh_plug1),
    path('toggle_plug2', plug2.toggle_plug2),
    path('refresh_plug2', plug2.refresh_plug2),
    path('toggle_switch1', switch1.toggle_switch1),
    path('refresh_switch1', switch1.refresh_switch1),
    path('toggle_switch2', switch2.toggle_switch2),
    path('refresh_switch2', switch2.refresh_switch2),
    path('toggle_switch3', switch3.toggle_switch3),
    path('refresh_switch3', switch3.refresh_switch3),
    path('toggle_switch4', switch4.toggle_switch4),
    path('refresh_switch4', switch4.refresh_switch4),
    path('toggle_switch5', switch5.toggle_switch5),
    path('refresh_switch5', switch5.refresh_switch5),
    path('plug1', views.plug1, name="plug1"),
    path('plug2', views.plug2, name="plug2"),
    path('switch1', views.switch1, name="switch1"),
    path('switch2', views.switch2, name="switch2"),
    path('switch3', views.switch3, name="switch3"),
    path('switch4', views.switch4, name="switch4"),
    path('switch5', views.switch5, name="switch5"),
]
