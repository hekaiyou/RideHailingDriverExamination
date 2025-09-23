from django.db import models


class Student(models.Model):

    class ProfessionType(models.TextChoices):
        RIDER = 'Rider', '网络预约出租汽车驾驶员'
        OTHER = 'Other', '其他'

    name = models.CharField(max_length=100, verbose_name='姓名')
    id_card = models.CharField(max_length=18, unique=True, verbose_name='身份证号')
    profession_type = models.CharField(max_length=100, choices=ProfessionType.choices, default=ProfessionType.RIDER, verbose_name='从业类型')
    password = models.CharField(max_length=20, verbose_name='密码', blank=True)

    def save(self, *args, **kwargs):
        # 如果密码未设置, 则使用身份证后6位作为默认密码
        if not self.password:
            self.password = self.id_card[-6:]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "学员"
        verbose_name_plural = "学员"


class Course(models.Model):

    class SubjectType(models.TextChoices):
        REGIONAL = 'Regional', '区域科目'
        PUBLIC = 'Public', '公共科目'

    name = models.CharField(max_length=255, verbose_name='课程名称')
    subject_type = models.CharField(max_length=20, choices=SubjectType.choices, verbose_name='科目类型')
    exam_subject = models.CharField(max_length=255, verbose_name='考试科目')
    question_count = models.IntegerField(verbose_name='试题数量')
    exam_time = models.IntegerField(verbose_name='考试时间(分钟)')
    score_per_question = models.FloatField(verbose_name='单题分值')
    passing_score = models.FloatField(verbose_name='通过分数')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程"


class Question(models.Model):
 
    class QuestionType(models.TextChoices):
        SINGLE_CHOICE = 'SingleChoice', '单选题'
        MULTIPLE_CHOICE = 'MultipleChoice', '多选题'
        TRUE_FALSE = 'TrueFalse', '判断题'
 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions', verbose_name='课程')
    text = models.TextField(verbose_name='题目描述')
    question_type = models.CharField(max_length=20, choices=QuestionType.choices, verbose_name='题目类型')
    # 适用于判断题的正确性字段
    is_correct = models.BooleanField(default=False, verbose_name='正确答案')
    # 适用于单选和多选题的选项
    option_a = models.CharField(max_length=255, blank=True, verbose_name='选项A')
    a_correct = models.BooleanField(default=False, verbose_name='选项A为正确答案')
    option_b = models.CharField(max_length=255, blank=True, verbose_name='选项B')
    b_correct = models.BooleanField(default=False, verbose_name='选项B为正确答案')
    option_c = models.CharField(max_length=255, blank=True, verbose_name='选项C')
    c_correct = models.BooleanField(default=False, verbose_name='选项C为正确答案')
    option_d = models.CharField(max_length=255, blank=True, verbose_name='选项D')
    d_correct = models.BooleanField(default=False, verbose_name='选项D为正确答案')
    option_e = models.CharField(max_length=255, blank=True, verbose_name='选项E')
    e_correct = models.BooleanField(default=False, verbose_name='选项E为正确答案')
    option_f = models.CharField(max_length=255, blank=True, verbose_name='选项F')
    f_correct = models.BooleanField(default=False, verbose_name='选项F为正确答案')
 
    def __str__(self):
        return self.text
 
    class Meta:
        verbose_name = "题目"
        verbose_name_plural = "题目"
