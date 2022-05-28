from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from threads.views import CreateThreadView
from threads.views import IndexView
from threads.views import ThreadDetailView

urlpatterns = [
    path('', IndexView.as_view()),
    path('create/', CreateThreadView.as_view()),
    path('thread/<int:id>/', ThreadDetailView.as_view()),
    path('tetra/', include('tetra.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
