from . import views

from django.urls import path

urlpatterns = [
    path('', views.SignInView.as_view(), name='login-page'),
    path('logout/', views.SignOutView.as_view(), name='logout-page'),
    path('applicants/', views.ApplicantsListView.as_view(), name="applicants-list"),
    path('applicants/<id>/resume/download/', views.download, name='resume-download'),
    path('applicant/<pk>/', views.ApplicantDetailView.as_view(), name='applicant-profile'),
    path('applicant/<id>/', views.ApplicantDeleteView.as_view(), name='applicant-delete')
]