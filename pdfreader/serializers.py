from rest_framework import serializers
from .models import ApplicantRecord

class PDFReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicantRecord
        fields = "__all__"
