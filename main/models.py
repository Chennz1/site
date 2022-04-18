from django.db import models
from sympy import content

# Create your models here.
# class userinfo(models.Model):
#     name=models.CharField(max_length=32)
    
    
    
'''
    
    creat table main_userinfo(
        id bigint auto_increment primary key,
        name varchar(32),
    )

    py manage.py makemigrations
    py manage.py migrate xxx

    '''
class Course(models.Model):#科目名字：英语数学等等，同用途
    # id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    url=models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kemu'
class Wangke(models.Model):
    # id = models.CharField(max_length=10, blank=True, null=True)
    courseid=models.ForeignKey(to="Course",to_field="id",on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=10, blank=True, null=True)
    level = models.IntegerField( blank=True, null=True)
    url=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wangke'
        
class Shuji(models.Model):
    # id = models.CharField(max_length=10, blank=True, null=True)
    courseid=models.ForeignKey(to="Course",to_field="id",on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=10, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shuji'

class Person(models.Model):
    # id = models.CharField(max_length=10, blank=True, null=True)
    passport = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=10, blank=True, null=True)
    direction = models.ForeignKey(to="Course",to_field="id",on_delete=models.DO_NOTHING)
    level = models.IntegerField( blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'

class Talk(models.Model):
    courseid = models.ForeignKey(to="Course",to_field="id",on_delete=models.DO_NOTHING)
    index = models.IntegerField(blank=True, null=True)
    personid = models.ForeignKey( to="Person",to_field="id",on_delete=models.DO_NOTHING)
    text=models.TextField(max_length=200,blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'talk'