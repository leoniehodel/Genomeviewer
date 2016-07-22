from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^genomebrowser/', include('genomebrowser.urls')),
    url(r'^trackhubs/', include('trackhubs.urls'))

]
