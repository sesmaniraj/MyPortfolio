from django.db import models

# Create your models here.
from django.db import models

        
        
class AboutMe(models.Model):
    name=models.CharField(max_length=200)
    short_intro=models.TextField()
    cv=models.FileField(upload_to="cv")
    phoneNo=models.PositiveBigIntegerField()
    address=models.CharField(max_length=300)
    completedProjects=models.PositiveBigIntegerField()
    clients=models.PositiveIntegerField()
    image=models.ImageField(upload_to="aboutme")
    facebookUrl=models.URLField(null=True,blank=True)
    instagramUrl=models.URLField(null=True,blank=True)
    linkendinUrl=models.URLField(null=True,blank=True)
    github=models.URLField(null=True,blank=True)
    gmail=models.EmailField()
    whatsApp=models.PositiveBigIntegerField(null=True,blank=True)
    locationUrl=models.URLField(max_length=1050)
    class Meta:
        ordering =['-id',]


    def __str__(self):
        return self.name
        
        

class Experience(models.Model):
    designation=models.CharField(max_length=300)
    companyName=models.CharField(max_length=300)
    startedDate=models.DateField()
    endDate=models.DateField(null=True,blank=True)
    short_description_about_work=models.TextField(null=True,blank=True)
    class Meta:
        ordering =['-id',]
        
        
    def __str__(self):
        return self.companyName


class Skills(models.Model):
    title=models.CharField(max_length=200)

    class Meta:
        ordering =['-id',]


    def __str__(self):
        return self.title
    
        
        
projecttype =(
    ('MobileApp',"Mobile Application"),
    ('Website',"Website"),
  
)


class Portfolio(models.Model):
    projectType =models.CharField(max_length=150, choices=projecttype)
    projectName=models.CharField(max_length=200)
    languageUsed=models.TextField()
    country=models.CharField(max_length=200)
    projectUrl=models.URLField(null=True,blank=True)
    short_description=models.TextField()

    class Meta:
        ordering =['-id',]
        
    def __str__(self):
        return self.projectName
    

class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.SET_NULL, null=True, blank=True, related_name ='portfolioimages')
    image = models.ImageField(upload_to='Portfolioimage/')


    class Meta:
        ordering  =['-id']


class Contact(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=500)
    email=models.EmailField()
    message=models.TextField()

    class Meta:
        ordering =['-id']
        
    def __str__(self):
        return self.name