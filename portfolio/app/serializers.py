from rest_framework import serializers
from .models import *

class PortfolioImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PortfolioImages
        fields = ('id', 'image')

class PortfolioSerializer(serializers.ModelSerializer):
    portfolioimages = PortfolioImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = '__all__'


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'