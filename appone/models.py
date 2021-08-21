from django.db import models

class StudentInfo(models.Model):
    Roll_no=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    Class=models.CharField(max_length=20)
    School=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=14)
    Address=models.CharField(max_length=20)

    class Meta:
        db_table='StudentInfo'

class StudentAcademics(StudentInfo):
    # Roll_no=models.ForeignKey(StudentInfo, on_delete=models.CASCADE,related_name='studref')
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()

    class Meta:
        db_table='StudentAcademics'


