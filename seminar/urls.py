from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('seminar/', views.ListSeminarView.as_view(), name='list-seminar'),
    path('seminar/<int:pk>/detail/', views.DetailSeminarView.as_view(), name='detail-seminar'),
    path('seminar/create/', views.CreateSeminarView.as_view(), name='create-seminar'),
    path('seminar/<int:pk>/delete/', views.DeleteSeminarView.as_view(), name='delete-seminar'),
    path('seminar/<int:pk>/update/', views.UpdateSeminarView.as_view(), name='update-seminar'),
    path('seminar/<int:seminar_id>/review/', views.CreateReviewView.as_view(), name='review'),

]

