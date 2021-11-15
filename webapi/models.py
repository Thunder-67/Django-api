from django.db import models
from django.db.models import Model

# Create your models here.
class categories(models.Model):
    strcategory=models.CharField(max_length=30)
    strcategorythumb=models.FileField(max_length=100)
    strcategorydescribtion=models.TextField()

    def __str__(self):
        return self.strcategory

class meals(models.Model):
    strmeal=models.CharField(max_length=100)
    strmealthumb=models.FileField(max_length=100)
    idmeal=models.IntegerField()

    def __str__(self):
        return self.strmeal

class search(models.Model):
    idmeal=models.IntegerField()
    strMeal=models.CharField(max_length=100)
    strDrinkAlternate=models.CharField(max_length=100,null=True,blank=True)
    strcategory=models.CharField(max_length=100)
    strArea=models.CharField(max_length=100)
    strInstruction=models.CharField(max_length=1000)
    strmealthumb=models.FileField(max_length=100)
    strTags=models.CharField(max_length=100)
    strYoutube=models.URLField(max_length=100)
    strIngridient1=models.CharField(max_length=100)
    strIngridient2=models.CharField(max_length=100)
    strIngridient3=models.CharField(max_length=100)
    strIngridient4=models.CharField(max_length=100)
    strIngridient5=models.CharField(max_length=100)
    strIngridient6=models.CharField(max_length=100)
    strIngridient7=models.CharField(max_length=100)
    strIngridient8=models.CharField(max_length=100)
    strIngridient9=models.CharField(max_length=100,blank=True)
    strIngridient10=models.CharField(max_length=100,blank=True)
    strIngridient11=models.CharField(max_length=100,blank=True)
    strIngridient12=models.CharField(max_length=100,blank=True)
    strIngridient13=models.CharField(max_length=100,blank=True)
    strIngridient14=models.CharField(max_length=100,blank=True)
    strIngridient15=models.CharField(max_length=100,blank=True)
    strIngridient16=models.CharField(max_length=100,blank=True)
    strIngridient17=models.CharField(max_length=100,blank=True)
    strIngridient18=models.CharField(max_length=100,blank=True)
    strIngridient19=models.CharField(max_length=100,blank=True)
    strIngridient20=models.CharField(max_length=100,blank=True)
    strMeasure1=models.CharField(max_length=100)
    strMeasure2=models.CharField(max_length=100)
    strMeasure3=models.CharField(max_length=100)
    strMeasure4=models.CharField(max_length=100)
    strMeasure5=models.CharField(max_length=100)
    strMeasure6=models.CharField(max_length=100)
    strMeasure7=models.CharField(max_length=100)
    strMeasure8=models.CharField(max_length=100)
    strMeasure9=models.CharField(max_length=100,blank=True)
    strMeasure10=models.CharField(max_length=100,blank=True)
    strMeasure11=models.CharField(max_length=100,blank=True)
    strMeasure12=models.CharField(max_length=100,blank=True)
    strMeasure13=models.CharField(max_length=100,blank=True)
    strMeasure14=models.CharField(max_length=100,blank=True)
    strMeasure15=models.CharField(max_length=100,blank=True)
    strMeasure16=models.CharField(max_length=100,null=True,blank=True)
    strMeasure17=models.CharField(max_length=100,blank=True)
    strMeasure18=models.CharField(max_length=100,blank=True)
    strMeasure19=models.CharField(max_length=100,blank=True)
    strMeasure20=models.CharField(max_length=100,blank=True)
    strsource=models.CharField(max_length=100,null=True,blank=True)
    strImageSource=models.CharField(max_length=100,null=True,blank=True)
    strCreativeCommonsConfirmed=models.CharField(max_length=100,null=True,blank=True)
    dateModified=models.CharField(max_length=100,null=True,blank=True)
