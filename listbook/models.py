from django.db import models 
class BoardsModel(models.Model): 
    titulo = models.CharField(max_length = 150) 
    autor = models.CharField(max_length = 150) 
    valoracion = models.IntegerField(range(0,10000)) 
def __str__(self): 
    return self.titulo