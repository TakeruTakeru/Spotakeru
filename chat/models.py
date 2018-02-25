from django.db import models

class Basic_data(models.Model):
    place_name = models.CharField(max_length=30)#地名
    travel_expenses = models.CharField(max_length=100)#旅費
    hotel_expenses = models.CharField(max_length=20)#滞在費
    religion = models.CharField(max_length=100)#地域
    info = models.TextField()#基礎情報


class Additional_data(models.Model):
    information = models.ForeignKey(Basic_data, on_delete=models.CASCADE)
    facilities = models.CharField(max_length=20)#イベントや施設など

    def __str__(self):
        return self.facilities
