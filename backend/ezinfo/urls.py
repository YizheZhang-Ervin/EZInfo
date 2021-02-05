from django.urls import path
from ezinfo.views import codingApi,translatorApi
from ezinfo.visualization import getDataFromDB,getDataFromWeb

app_name="ezinfo"
urlpatterns = [
    path('api/ssec/', getDataFromDB),
    path('api/ssec/update/',getDataFromWeb),
    path('api/coding/', codingApi.as_view()),
    path('api/translate/', translatorApi.as_view()),
]