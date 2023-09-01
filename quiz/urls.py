from django.urls import path
from . import views

urlpatterns = [
    
    path("<int:myid>/", views.quiz, name="quiz"), 
    path('<int:myid>/data/', views.quiz_data_view, name='quiz-data'),

    path('<int:myid>/save/', views.save_quiz_view, name='quiz-save'),
    path('', views.index, name='quiz_index'),
    path('result_delete/<int:myid>/', views.result_delete, name='result_delete'),
    path('delete_question/<int:myid>/', views.delete_question, name='delete_question'),  

    
    
    
    path('quiz/add_quiz/', views.add_quiz, name='add_quiz'),    
    path('quiz/add_question/', views.add_question, name='add_question'),  
    path('add_options/<int:myid>/', views.add_options, name='add_options'), 
    path('quiz/results/', views.results, name='results'),    

   


       
]