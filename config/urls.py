from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('network/', include('network.urls', namespace='network')),
                  # path('contacts/', include('contacts.urls', namespace='contacts')),
                  # path('products/', include('products.urls', namespace='products')),
                  # path('users/', include('users.urls', namespace='users')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
