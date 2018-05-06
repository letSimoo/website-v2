from django.urls import path, include

from . import api


api_urls = [
    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/lessons/',
         api.LessonListAPIView.as_view(),
         name='lesson_list_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/lessons/<slug:lesson_slug>/',
         api.LessonRetrieveAPIView.as_view(),
         name='lesson_retrieve_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/',
         api.ModuleListAPIView.as_view(),
         name='module_liste_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/',
         api.ModuleRetrieveAPIView.as_view(),
         name='module_retrieve_api'),

    path('tracks/<slug:track_slug>/workshops/',
         api.WorkshopListAPIView.as_view(),
         name='workshops_list_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>',
         api.WorkshopRetrieveAPIView.as_view(),
         name='workshops_retrieve_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_api'),

    path('tracks/<slug:slug>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_api'),
]

urlpatterns = [
    path('', include(api_urls))
]
