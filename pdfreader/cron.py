from django_cron import CronJobBase, Schedule
from .pdf2 import get_applicants_data
from .models import ApplicantRecord

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'pdfreader.my_cron_job'    # a unique code

    def do(self):
        data = get_applicants_data()
        for dt in data:
            data_record = ApplicantRecord(
                reg_num=dt["reg_num"],
                name=dt["name"],
                state=dt["state"],
                categories=dt["categories"],
                sex=dt["sex"]
                )
            data_record.save()

# run python3 manage.py runcrons -> to add data to db