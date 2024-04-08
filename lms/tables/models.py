from django.db import models

# Create your models here.

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    
    
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=10, unique=True)
    

class Assesment_Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.TextField(unique=True)
    

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=1, unique=True)


class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, unique=True)
    subject_score = models.FloatField()
    
    

class Summary(models.Model):
    school_id = models.IntegerField()
    sydney_participants = models.IntegerField()
    sydney_percentile = models.FloatField()
    assesment_area_id = models.IntegerField()
    awards_id = models.IntegerField()
    class_id = models.IntegerField()
    correct_answer_percentage_per_class = models.FloatField()
    correct_answers = models.CharField(max_length=1)
    student_id = models.IntegerField()
    participant = models.IntegerField()
    student_score = models.FloatField()
    subject_id = models.IntegerField()
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer_id = models.IntegerField()
    correct_answers_id = models.IntegerField()
