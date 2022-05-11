from django.db import models

# author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
# slug = models.SlugField(unique=True, null=True)
slug = models.SlugField(unique=True)
# Create your models here. or  Schema 
class Poll(models.Model):
    question= models.TextField()

    question_one=models.CharField(max_length=80)
    question_two=models.CharField(max_length=80)
    question_three=models.CharField(max_length=80)
    # question_four=models.CharField(max_length=80)

    question_one_count=models.IntegerField(default=0)
    question_two_count=models.IntegerField(default=0)
    question_three_count=models.IntegerField(default=0)
    question_four_count=models.IntegerField(default=0)
