from django.db import models

# Create your models here.


class ApplicantRecord(models.Model):
    reg_num = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    state = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        applicant_names = self.name.split(" ")
        self.first_name = applicant_names[0]
        if len(applicant_names) >= 3:
            self.last_name = applicant_names[2]
        else:
            self.last_name = applicant_names[1]
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@utilibox.co"
        super(ApplicantRecord, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

