
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from classes_api.views import List, Detail, Create, Update, Delete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('api/list/', List.as_view(), name='list'),
    path('api/detail/', Detail.as_view(), name='detail'),
    path('api/create/', Create.as_view(), name='create'),
    path('api/<int:classroom_id>/update/', Update.as_view(), name='update'),
    path('api/<int:classroom_id>/delete/', Delete.as_view(), name='delete'),



]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
