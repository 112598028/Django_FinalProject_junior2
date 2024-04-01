from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=256, null=True)
    password = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # 額外資訊，排序方式、使用資料表...
    
    def __str__(self):
        return f"Title: {self.name}"
    
    class Meta:
        ordering = ["name"]
        db_table = 'members'
