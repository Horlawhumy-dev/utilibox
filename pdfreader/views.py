from sys import excepthook
from warnings import filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import ApplicantsPaginatedClass

from .serializers import PDFReaderSerializer
from .models import ApplicantRecord


class GetAllApplicantsData(APIView):

    permission_classes = []
   
    def get(self, request, *args, **kwargs):
        try:
            data = ApplicantRecord.objects.all()
        except Exception as err:
            return Response("Unable to fetch data records from database.", status=500)
        paginated_data = ApplicantsPaginatedClass().paginate_queryset(data, request=request, view=self)
        serializer = PDFReaderSerializer(paginated_data, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class GetApplicant(APIView):

    permission_classes = []

    def get(self, request, pk, format=None):
        try:
            employee = ApplicantRecord.objects.get(id=pk)
        except Exception as err:
            return Response("Applicant record does not exist", status=404)
            
        serializer = PDFReaderSerializer
        if serializer.is_valid:
            data = serializer(employee, many=False).data
            if data:
                return Response(data, status=200)
        return Response(serializer.errors, status=400)


class UpdateApplicantRecord(APIView):

     permission_classes = []

     def put(self, request, pk, *args, **kwargs):
        try:   
            comment = ApplicantRecord.objects.get(pk=pk)
        except Exception as err:
            return Response("Applicant record does not exist", status=404)
        data = request.data
        serializer = PDFReaderSerializer
        serializer = serializer(instance=comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data=dict(
                    status="success",
                    message=f"Applicant with id {pk} is successfully updated!"
                ),
                status=200)
        return Response(
            data=dict(
                status="Failed",
                message=f"Applicant with id {pk} is not successfully updated!"
            ),
            status=400)


class DeleteApplicantRecord(APIView):

     permission_classes = []

     def delete(self, request, pk, *args, **kwargs):
        try:
            comment = ApplicantRecord.objects.get(pk=pk)
        except Exception as err:
            return Response("Applicant record does not exist", status=404)

        comment.delete()

        return Response(
            data=dict(
                status="success",
                message=f"Applicant with id {pk} is successfully deleted!"
            ),
            status=200)