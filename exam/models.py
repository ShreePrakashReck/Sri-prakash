from django.db import models
class students(models.Model):
    rollnumber= models.IntegerField()
    studentname= models.CharField(max_length=40)
    studentBranch= models.CharField(max_length=80)
    studentyear= models.IntegerField()
    def __str__(self):
        return self.studentname
