from importlib.resources import path
from django.urls import path

from pdfreader import views


urlpatterns = [
    path('applicants/data', views.GetAllApplicantsData.as_view(), name="all-data"),
    path('applicants/data/<int:pk>', views.GetApplicant.as_view(), name="applicant"),
    path('applicants/data/update/<int:pk>', views.UpdateApplicantRecord.as_view(), name="update-record"),
    path('applicants/data/delete/<int:pk>', views.DeleteApplicantRecord.as_view(), name="delete-record")
]