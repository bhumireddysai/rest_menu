from django.db import models

# Create your models here.


class sections(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=200)


class items(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    descriptions = models.CharField(max_length=200)
    price = models.IntegerField()
    section_id = models.ForeignKey(sections, db_column='section_id',on_delete=models.CASCADE)

class modifiers(models.Model):
    Id = models.AutoField(primary_key=True)
    descriptions = models.CharField(max_length=200)
    items_id = models.ForeignKey(items, db_column='items_id',on_delete=models.CASCADE)

