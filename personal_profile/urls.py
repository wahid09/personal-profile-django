import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
    path('account/', include('Login_App.urls')),
    path('blog/', include('Blog_App.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
