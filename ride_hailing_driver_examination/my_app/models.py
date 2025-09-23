from django.db import models

class Student(models.Model):

    class ProfessionType(models.TextChoices):
        RIDER = 'Rider', '网络预约出租汽车驾驶员'
        OTHER = 'Other', '其他'

    id_card = models.CharField(max_length=18, unique=True, verbose_name='身份证号')
    profession_type = models.CharField(max_length=100, choices=ProfessionType.choices, default=ProfessionType.RIDER, verbose_name='从业类型')

    def __str__(self):
        return self.id_card

    class Meta:
        verbose_name = "学员"
        verbose_name_plural = "学员"
