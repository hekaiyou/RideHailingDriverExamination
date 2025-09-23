from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 用户从业类型的枚举
    class OccupationType(models.TextChoices):
        RIDER = 'Rider', '网络预约出租汽车驾驶员'
        OTHER = 'Other', '其他'

    id_card = models.CharField(max_length=18, unique=True, verbose_name='身份证号')
    occupation_type = models.CharField(
        max_length=30,
        choices=OccupationType.choices,
        default=OccupationType.RIDER,
        verbose_name='从业类型'
    )

    def __str__(self):
        return self.username
