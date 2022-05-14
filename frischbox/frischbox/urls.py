from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('contact', views.contactform, name='contactform'),
    path('about/', views.about, name='about'),
    path('bulk', views.bulk, name='bulk'),
    path('status', views.status, name='status'),
    path('cities', views.cities, name='cities'),
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('policy/<postid>', views.policydetails, name='policydetails'),

    # Cart Paths



    # Blog Module Path
    path('blog/', views.blog, name='blog'),
    path('blog/<postid>', views.postdetails, name='postdetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

