from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from posts.views import post_list_view
from posts.views import post_detail_view

from pages.views import home_view
from pages.views import about_view
from pages.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('detail/<int:detail_id>', post_detail_view, name='detail'),
    path('all/', post_list_view, name='all')

]

urlpatterns += staticfiles_urlpatterns()
