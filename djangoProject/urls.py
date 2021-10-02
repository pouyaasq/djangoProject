from django.contrib import admin
from django.urls import path ,include
from . import view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings#tamam ghesmat haye seting ro be url motasel mikonad
from django.conf.urls.static import static
from articels.views import articel_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('articels.urls')),
    path('accounts/', include('accounts.urls')),
    path('', articel_list),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
