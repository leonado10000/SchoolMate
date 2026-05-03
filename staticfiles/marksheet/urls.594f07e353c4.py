from django.urls import path
from .views import marksheet_view, all_current_terms, scorecard_pdf_download, student_scorecard, marksheet_pdf_download

urlpatterns = [
    path('terms', all_current_terms, name='all_current_terms'),
    path('marksheet_view/<str:sheet_id>', marksheet_view, name='marksheet_view'),
    path('download/<str:marksheet_id>', marksheet_pdf_download, name="marksheet_download"),
    path('student/<str:student_id>', student_scorecard, name="student_scorecard"),
    path('download/<str:student_id>/<int:sem>', scorecard_pdf_download, name="scorecard_download")
]