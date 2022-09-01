from django.db import models

# Create your models here.

class Stories(models.Model):
    authorFname = models.CharField(max_length=256,null=False, blank=True)
    authorLname = models.CharField(max_length=256,null=False, blank=True)
    authorEmail = models.CharField(max_length=256,null=False, blank=True)
    authorNumber = models.CharField(max_length=256,null=True, blank=True)
    scamTitle = models.CharField(max_length=256,null=True, blank=True)
    scamType = models.CharField(max_length=256,null=False, blank=True)
    nameOfScamer = models.CharField(max_length=256,null=True, blank=True)
    contentOfScamer = models.CharField(max_length=256,null=True, blank=True)
    emailOfScamer = models.CharField(max_length=256,null=True, blank=True)
    scamDetail = models.TextField(unique=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.authorEmail

class Cooperation(models.Model):
    organisationName = models.CharField(max_length=256,null=False, blank=True)
    organisationEmail = models.CharField(max_length=256,null=False, blank=True)
    personInContact = models.CharField(max_length=256,null=False, blank=True)
    ContactNumber = models.CharField(max_length=256,null=False, blank=True)
    cooperationDetail = models.TextField(unique=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organisationName

class JoinActivites(models.Model):
    activitesTitle = models.CharField(max_length=256,null=False, blank=True)
    joinerName = models.CharField(max_length=256,null=False, blank=True)
    joinerEmail = models.CharField(max_length=256,null=False, blank=True)
    joinerContactNumber = models.CharField(max_length=256,null=False, blank=True)
    joinerDob = models.CharField(max_length=256,null=False, blank=True)
    joinAs = models.CharField(max_length=256,null=False, blank=True)

    def __str__(self):
        return self.joinerName

class AddActivites(models.Model):
    activitesTitle = models.CharField(max_length=256,null=False, blank=True)
    activitesDetail = models.TextField(unique=False,blank=False)
    activitesLocation = models.CharField(max_length=256,null=False, blank=True)
    activitesCooperateWith = models.CharField(max_length=256,null=False, blank=True)
    activitesDate = models.CharField(max_length=256,null=False, blank=True)
    activitesTime = models.CharField(max_length=256,null=False, blank=True)
    toDo = models.TextField(unique=False,null=False,blank=True)
    canJoinAs = models.TextField(unique=False,null=False,blank=True)


    def __str__(self):
        return self.activitesTitle