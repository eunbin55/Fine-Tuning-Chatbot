from django.db import models

# Create your models here.

class BoardPost (models.Model):
    title= models.CharField(max_length=200)
    content=models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self) :
#         return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.title
    
# 세부모델
class FineTunedModel(models.Model):
    MODEL_CHOICES =[
        ('ada','Ada'),
        ('babbage','Babbage'),
        ('curie', 'Curie'),
        ('davinci','Davinci'),
    ]

    model_name = models.CharField(max_length=100)
    base_model=models.CharField(max_length=100, choices=MODEL_CHOICES)

    def __str__(self):
        return self.model_name
  
#   특정 세부 모델과 연결된 훈련 데이터
class TrainingData(models.Model):
    fine_tuned_model =models.ForeignKey(FineTunedModel,  on_delete=models.CASCADE, related_name='training_data')
    prompt = models.TextField()
    completion=models.TextField()

    def __str__(self):
        return f"{self.fine_tuned_model.model_name}의 훈련 데이터"
    