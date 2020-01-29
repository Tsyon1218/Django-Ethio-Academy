
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('contact/', include('Contact.urls')),
    path('RegisterStudent/',include('RegisterStudent.urls')),
    path('SAMPLE/',include('SAMPLE.urls')),
    path('Blog/',include('Blog.urls')),
    path('RegisterVaccancy/',include('RegisterVaccancy.urls')),
    path('About/',include('About.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)