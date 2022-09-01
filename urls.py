from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('scamType/', views.scamType, name='scamType'),
    path('typeDetail1/', views.typeDetail1, name='typeDetail1'),
    path('typeDetail2/', views.typeDetail2, name='typeDetail2'),
    path('typeDetail3/', views.typeDetail3, name='typeDetail3'),
    path('typeDetail4/', views.typeDetail4, name='typeDetail4'),
    path('stories/', views.stories, name='stories'),
    path('mediaNews/', views.mediaNews, name='mediaNews'),
    path('addStory/', views.addStory, name='addStory'),
    path('addStoryAction/', views.addStoryAction, name='addStoryAction'),
    path('activities/', views.activitiesList.as_view(), name='activities'),
    path('activitiesDetail1/', views.activitiesDetail1, name='activitiesDetail1'),
    path('activitiesDetail2/', views.activitiesDetail2, name='activitiesDetail2'),
    path('cooperation/', views.cooperation, name='cooperation'),
    path('addCooperationAction/', views.addCooperationAction, name='addCooperationAction'),
    path('addJoinActivitesAction/', views.addJoinActivitesAction, name='addJoinActivitesAction'),
    path('activity/<int:pk>',  views.ActivitesDetail.as_view(), name='activity'),
    path('api/stories_api', api.StoriesList.as_view(), name='stories_api'),
    path('api/stories_api/<int:pk>', api.StoriesDetails.as_view(), name='stories_api_detail'),
    path('api/cooperation_api', api.CooperationList.as_view(), name='cooperation_api'),
    path('api/JoinActivites_api', api.JoinActivitesList.as_view(), name='JoinActivites_api'),
    
   
]
