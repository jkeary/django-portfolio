from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import project.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project.views.home, name='home'),
    path('projects/', include('project.urls')),
    path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
