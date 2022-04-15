from statistics import mode
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User



class profileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255, default="", null=True,blank=True)
    middle_name = models.CharField(max_length=255, default="", null=True,blank=True)
    last_name = models.CharField(max_length=255, default="", null=True,blank=True)
    dept = models.CharField(max_length=255,default="",blank=True)
    enrollment = models.CharField(max_length=255,default="",blank=True)
    batch = models.CharField(max_length=255,default="",blank=True)
    nick_name = models.CharField(max_length=255, default="", null=True,blank=True)
    date_of_birth = models.CharField(max_length=255,default="", null=True,blank=True)
    place_of_birth = models.CharField(max_length=255,default="", null=True,blank=True)
    gender = models.CharField(max_length=255,default="", null=True,blank=True)
    marital_status = models.CharField(max_length=255,default="", null=True,blank=True)
    blood_group = models.CharField(max_length=255,default="", null=True,blank=True)
    religion = models.CharField(max_length=255,default="", null=True,blank=True)
    nationality = models.CharField(max_length=255,default="", null=True,blank=True)
    national_id = models.CharField(max_length=255,default="", null=True,blank=True)
    passport_no = models.CharField(max_length=255,default="", null=True,blank=True)
    social_network_id = models.CharField(max_length=255,default="", null=True,blank=True)
    im = models.CharField(max_length=255,default="", null=True,blank=True)
    about_you = models.CharField(max_length=255,default="", null=True,blank=True)
    mobile = models.CharField(max_length=255,default="", null=True,blank=True)
    present_mobile = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_mobile = models.CharField(max_length=255,default="", null=True,blank=True)
    email = models.CharField(max_length=255,default="", null=True,blank=True)
    alternative_email = models.CharField(max_length=255,default="", null=True,blank=True)
    father_name = models.CharField(max_length=255,default="", null=True,blank=True)
    father_contact_no = models.CharField(max_length=255,default="", null=True,blank=True)
    father_occupation = models.CharField(max_length=255,default="", null=True,blank=True)
    father_designation = models.CharField(max_length=255,default="", null=True,blank=True)
    father_employers_name = models.CharField(max_length=255,default="", null=True,blank=True)
    father_eannual_income = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_name = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_contact_no = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_occupation = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_designation = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_employer_name = models.CharField(max_length=255,default="", null=True,blank=True)
    mother_annual_income = models.CharField(max_length=255,default="", null=True,blank=True)
    parents_address = models.CharField(max_length=255,default="", null=True,blank=True)
    local_guardian_name = models.CharField(max_length=255,default="", null=True,blank=True)
    local_guardian_contact_no = models.CharField(max_length=255,default="", null=True,blank=True)
    relation_with_local_guardian = models.CharField(max_length=255,default="", null=True,blank=True)
    local_guardian_address = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_post_office = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_police_station = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_district = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_division = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_country = models.CharField(max_length=255,default="", null=True,blank=True)
    present_address_zipcode = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_post_office = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_police_station = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_district = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_division = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_country = models.CharField(max_length=255,default="", null=True,blank=True)
    permanent_address_zipcode = models.CharField(max_length=255,default="", null=True,blank=True)
    hostel_address = models.CharField(max_length=255,default="", null=True,blank=True)
    mess_address = models.CharField(max_length=255,default="", null=True,blank=True)
    other_address = models.CharField(max_length=255,default="", null=True,blank=True)
    

    def __str__(self):
        return f'{self.user} profile'


class result(models.Model):
    studentid = models.CharField(max_length=100,default="")
    CHOICES = (
        ('Fall 2019', 'Fall 2019'),
        ('Fall 2021', 'Fall 2021'),
        ('Spring 2022', 'Spring 2022'),
        
    ) 

    semester = models.CharField(max_length=100,choices = CHOICES,default="")
    courseTitle = models.CharField(max_length=255,default="")
    courseCode = models.CharField(max_length=255,default="")
    credit = models.CharField(max_length=255,default="")
    grade = models.CharField(max_length=255,default="")
    gradepoint = models.CharField(max_length=255,default="")

    def __str__(self):
        return f'{self.studentid} {self.semester}'


class cgpa(models.Model):
    student_id = models.CharField(max_length=255,default="")
    semestername = models.CharField(max_length=255,default="")
    total_credit = models.IntegerField()
    sgpa = models.CharField(max_length=200,default="")

    def __str__(self):
        return f'{self.semestername} {self.student_id} cgpa'


class paymentdesc(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    total_payable = models.CharField(max_length=255,default="")
    total_paid = models.CharField(max_length=255,default="")
    total_due = models.CharField(max_length=255,default="")
    total_others = models.CharField(max_length=255,default="")

    def __str__(self):
        return f'{self.user} payment'

class sgpadashboard(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    fall_19 = models.FloatField()
    fall_21 = models.FloatField()
    spring_22 = models.FloatField()

    def __str__(self):
        return f'{self.user}'