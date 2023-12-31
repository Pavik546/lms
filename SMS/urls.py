from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler400
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('programs/', include('course.urls')),
    path('result/', include('result.urls')),
    path('search/', include('search.urls')),
    path('quiz/', include('quiz.urls')),
  
    path('<int:pk>/<int:fee>/pay/', include('base.urls')),
    path('success/<int:pk>/', views.success, name='success'),
    path('markview/<str:str1>/<str:str2>/<int:pk>/<int:p>/<int:s>/<int:m>/',views.markview,name='markview'), 


   

    path('quizzes/accounts/api/', include('accounts.api.urls', namespace='accounts-api')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'app.views.handler404'
# handler500 = 'app.views.handler500'
# handler400 = 'app.views.handler400'
