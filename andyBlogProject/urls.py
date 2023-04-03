
from django.contrib import admin
from django.urls import path, include 

from andyBlogApp.views import frontpage, post_detail

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"),
    path('markdownx/', include('markdownx.urls')), 
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)