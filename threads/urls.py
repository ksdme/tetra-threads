from django.contrib import admin
from django.urls import path
from threads.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
]
