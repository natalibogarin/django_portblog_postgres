from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='apps.blog'

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:id>/", views.blog_detail, name="blog_detail"),
    url("post/new", views.CreatePostView.as_view(), name='CreatePostView'),
    url('comment/<int:id>/approve', views.comment_approve, name='comment_approve'),
    url('comment/<int:id>/remove', views.comment_remove, name='comment_remove'),
    path('contacto', views.contact, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
