from django.urls import path
from .views import (
    add_score, add_score_for, grade_result, assessment_result, 
    course_registration_form, result_sheet_pdf_view,student1,studentlist
)


urlpatterns = [
    path('manage-score/', add_score, name='add_score'),
    path('student1/', student1, name='student1'),
    path('manage-score/<int:id>/', add_score_for, name='add_score_for'),
    path('student/<int:id>/', studentlist, name='studentlist'),
    
    path('grade/', grade_result, name="grade_results"),
    path('assessment/', assessment_result, name="ass_results"),

	path('result/print/<int:id>/', result_sheet_pdf_view, name='result_sheet_pdf_view'),
	path('registration/form/', course_registration_form, name='course_registration_form'),
]
