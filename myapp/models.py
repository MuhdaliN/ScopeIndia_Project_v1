from django.db import models

# Create your models here.    
class Studentsdbase(models.Model):
        gender=[
            ("M","male"),
            ("F","female"),
            ("O","other"),
        ]
        hobbies=[
            ("R","Reading"),
            ("T","Traveling"),
            ("S","Sports"),
            ("M","Music"),
            ]
        fname_db = models.CharField(max_length=100, blank=True, null=True)
        lname_db = models.CharField(max_length=100, blank=True, null=True)
        dob_db = models.DateField(blank=True, null=True)
        email_db = models.EmailField(blank=True, null=True)
        otp_db=models.CharField(max_length=25,default="NA",blank=True)
        password_db=models.CharField(max_length=255,blank=True)
        phone_db = models.CharField(max_length=15, blank=True, null=True)
        gender_db = models.CharField(max_length=10, blank=True, null=True)
        country_db = models.CharField(max_length=100, blank=True, null=True)
        state_db = models.CharField(max_length=100, blank=True, null=True)
        city_db = models.CharField(max_length=100, blank=True, null=True)
        hobbies_db = models.JSONField(default=list, blank=True)
        courses_db = models.TextField(blank=True, null=True)
        file_db = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

        class meta:
            verb_name_plural="Student_db1"
        def __str__(self):
            return self.fname_db
        
