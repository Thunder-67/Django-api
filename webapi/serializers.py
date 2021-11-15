from rest_framework import serializers
from .models import categories,meals,search

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    strcategory=serializers.CharField(max_length=30)
    strcategorythumb=serializers.FileField(max_length=100)
    strcategorydescribtion=serializers.CharField(max_length=300)
    class Meta:
        model=categories
        fields='__all__'

class mealsSerializer(serializers.HyperlinkedModelSerializer):
    strmeal=serializers.CharField(max_length=100)
    strmealthumb=serializers.FileField(max_length=100)
    idmeal=serializers.IntegerField()
    class Meta:
        model=meals
        fields='__all__'

class searchSerializer(serializers.HyperlinkedModelSerializer):
    idmeal=serializers.IntegerField()
    strMeal=serializers.CharField(max_length=100)
    strDrinkAlternate=serializers.CharField(max_length=100)
    strcategory=serializers.CharField(max_length=100)
    strArea=serializers.CharField(max_length=100)
    strInstruction=serializers.CharField(max_length=1000)
    strmealthumb=serializers.FileField(max_length=100)
    strTags=serializers.CharField(max_length=100)
    strYoutube=serializers.URLField(max_length=100)
    strIngridient1=serializers.CharField(max_length=100)
    strIngridient2=serializers.CharField(max_length=100)
    strIngridient3=serializers.CharField(max_length=100)
    strIngridient4=serializers.CharField(max_length=100)
    strIngridient5=serializers.CharField(max_length=100)
    strIngridient6=serializers.CharField(max_length=100)
    strIngridient7=serializers.CharField(max_length=100)
    strIngridient8=serializers.CharField(max_length=100)
    strIngridient9=serializers.CharField(max_length=100)
    strIngridient10=serializers.CharField(max_length=100)
    strIngridient11=serializers.CharField(max_length=100)
    strIngridient12=serializers.CharField(max_length=100)
    strIngridient13=serializers.CharField(max_length=100)
    strIngridient14=serializers.CharField(max_length=100)
    strIngridient15=serializers.CharField(max_length=100)
    strIngridient16=serializers.CharField(max_length=100)
    strIngridient17=serializers.CharField(max_length=100)
    strIngridient18=serializers.CharField(max_length=100)
    strIngridient19=serializers.CharField(max_length=100)
    strIngridient20=serializers.CharField(max_length=100)
    strMeasure1=serializers.CharField(max_length=100)
    strMeasure2=serializers.CharField(max_length=100)
    strMeasure3=serializers.CharField(max_length=100)
    strMeasure4=serializers.CharField(max_length=100)
    strMeasure5=serializers.CharField(max_length=100)
    strMeasure6=serializers.CharField(max_length=100)
    strMeasure7=serializers.CharField(max_length=100)
    strMeasure8=serializers.CharField(max_length=100)
    strMeasure9=serializers.CharField(max_length=100)
    strMeasure10=serializers.CharField(max_length=100)
    strMeasure11=serializers.CharField(max_length=100)
    strMeasure12=serializers.CharField(max_length=100)
    strMeasure13=serializers.CharField(max_length=100)
    strMeasure14=serializers.CharField(max_length=100)
    strMeasure15=serializers.CharField(max_length=100)
    strMeasure16=serializers.CharField(max_length=100)
    strMeasure17=serializers.CharField(max_length=100)
    strMeasure18=serializers.CharField(max_length=100)
    strMeasure19=serializers.CharField(max_length=100)
    strMeasure20=serializers.CharField(max_length=100)
    strsource=serializers.CharField(max_length=100)
    strImageSource=serializers.CharField(max_length=100)
    strCreativeCommonsConfirmed=serializers.CharField(max_length=100)
    dateModified=serializers.CharField(max_length=100)
    class Meta:
        model=search
        fields='__all__'