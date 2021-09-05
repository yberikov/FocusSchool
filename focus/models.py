from django.contrib.auth.models import User
from django.db import models


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_middlename = models.CharField(max_length=150, )
    user_level = models.IntegerField(verbose_name='Статус')

    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.user.first_name, self.user.last_name)


class Subject(models.Model):
    subject_name = models.CharField(max_length=150, )

    def __str__(self):
        return self.subject_name


class SchoolYear(models.Model):
    schoolyear_name = models.CharField(max_length=150, )

    def __str__(self):
        return self.schoolyear_name


class Pdg(models.Model):
    pdg_goal = models.CharField(max_length=1000, )
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    halfyear = models.IntegerField(verbose_name='Полугодие', )

    def __str__(self):
        return self.pdg_goal


class Classes(models.Model):
    class_name = models.CharField(max_length=15, )

    def __str__(self):
        return self.class_name


PLAN_CHOICES = (
    (1, "Самостоятельно разработанного урока"),
    (2, "Совместно разработанного с коллегами урока в рамках исследования урока"),
    (3, "Урока в рамках исследования практики"),
    (4, "Урока по авторской программе"),
    (5, "Урока по авторской методике")
)

MATERIAL_CHOICES = (
    (1, "Взаимосвязь темы с другими темами и разделами учебной программы"),
    (2, "Преемственность темы урока и непрерывности ее изучения"),
    (3, "Межпредметные связи учебной программы"),
    (4, "Идеи авторской программы"),
    (5, "Идеи авторской методики")
)

class FocusPlan1(models.Model):
    user_teacher = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='teacher_plan')
    user_observer = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='observer_plan')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='1')
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, default='1')
    fp1_date = models.DateField(auto_now=True)
    pdg = models.ForeignKey(Pdg, on_delete=models.CASCADE, default='1')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default='1')
    fp1_lessontopic = models.CharField(max_length=150, default=' ')
    fp1_item1 = models.IntegerField(choices=PLAN_CHOICES, default=1)
    fp1_item2 = models.BooleanField(default=True)
    fp1_item2_comm = models.CharField(max_length=150, default=' ', blank=True)
    fp1_item3 = models.BooleanField(default=True)
    fp1_item3_comm = models.CharField(max_length=150, default=' ', blank=True)
    fp1_item4 = models.IntegerField(choices=MATERIAL_CHOICES, default=1)
    fp1_item5 = models.BooleanField(default=True)
    fp1_item5_comm = models.CharField(max_length=150, default=' ', blank=True)
    fp1_item6 = models.BooleanField(default=True)
    fp1_item6_comm = models.CharField(max_length=150, default=' ', blank=True)
    fp1_item7 = models.BooleanField(default=True)
    fp1_item7_comm = models.CharField(max_length=150, default=' ', blank=True)
    fp1_review = models.CharField(max_length=150, default=' ')
    fp1_review_pdg = models.CharField(max_length=150, default=' ')
    fp1_additional = models.CharField(max_length=150, default=' ')

TEACH_CHOICE = (
    (1, "Удовлетворение потребностей учащихся"),
    (2, "Развитие способностей учащихся"),
    (3, "Развитие исследовательских навыков"),
    (4, "Развитие проектно- исследовательских навыков"),
    (5, "Развитие навыков проектной деятельности")
)
class FocusTeach1(models.Model):
    user_teacher = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='teacher_teach')
    user_observer = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='observer_teach')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='1')
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, default='1')
    ft1_date = models.DateField(auto_now=True)
    pdg = models.ForeignKey(Pdg, on_delete=models.CASCADE, default='1')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default='1')
    ft1_lessontopic = models.CharField(max_length=150, default=' ')
    ft1_item1 = models.IntegerField(choices=PLAN_CHOICES, default=1)
    ft1_item2 = models.BooleanField(default=True)
    ft1_item2_comm = models.CharField(max_length=150, default=' ', blank=True)
    ft1_item3 = models.BooleanField(default=True)
    ft1_item3_comm = models.CharField(max_length=150, default=' ', blank=True)
    ft1_item4 = models.IntegerField(choices=MATERIAL_CHOICES, default=1)
    ft1_item5 = models.BooleanField(default=True)
    ft1_item5_comm = models.CharField(max_length=150, default=' ', blank=True)
    ft1_item6 = models.IntegerField(choices=TEACH_CHOICE, default=1)
    ft1_review = models.CharField(max_length=150, default=' ')
    ft1_review_pdg = models.CharField(max_length=150, default=' ')
    ft1_additional = models.CharField(max_length=150, default=' ')



class FocusEvaluation1(models.Model):
    user_teacher = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='teacher_evaluation')
    user_observer = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='observer_evaluation')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='1')
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, default='1')
    fe1_date = models.DateField(auto_now=True)
    pdg = models.ForeignKey(Pdg, on_delete=models.CASCADE, default='1')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default='1')
    fe1_lessontopic = models.CharField(max_length=150, default=' ')
    fe1_item1 = models.BooleanField(default=True)
    fe1_item1_comm = models.CharField(max_length=150, default=' ', blank=True)
    fe1_item2 = models.BooleanField(default=True)
    fe1_item2_comm = models.CharField(max_length=150, default=' ', blank=True)
    fe1_item3 = models.BooleanField(default=True)
    fe1_item3_comm = models.CharField(max_length=150, default=' ', blank=True)
    fe1_item4 = models.BooleanField(default=True)
    fe1_item4_comm = models.CharField(max_length=150, default=' ', blank=True)
    fe1_item5 = models.BooleanField(default=True)
    fe1_item5_comm = models.CharField(max_length=150, default=' ', blank=True)
    fe1_review = models.CharField(max_length=150, default=' ')
    fe1_review_pdg = models.CharField(max_length=150, default=' ')
    fe1_additional = models.CharField(max_length=150, default=' ')

class FocusComplex1(models.Model):
    user_teacher = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='teacher_complex')
    user_observer = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='observer_complex')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='1')
    schoolyear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, default='1')
    fc1_date = models.DateField(auto_now=True)
    pdg = models.ForeignKey(Pdg, on_delete=models.CASCADE, default='1')
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default='1')
    fc1_lessontopic = models.CharField(max_length=150, default=' ')
    fc1_item1 = models.IntegerField(choices=PLAN_CHOICES, default=1)
    fc1_item2 = models.BooleanField(default=True)
    fc1_item2_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item3 = models.BooleanField(default=True)
    fc1_item3_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item4 = models.BooleanField(default=True)
    fc1_item4_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item5 = models.IntegerField(choices=MATERIAL_CHOICES, default=1)
    fc1_item6 = models.BooleanField(default=True)
    fc1_item6_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item7 = models.IntegerField(choices=TEACH_CHOICE, default=1)
    fc1_item8 = models.BooleanField(default=True)
    fc1_item8_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item9 = models.BooleanField(default=True)
    fc1_item9_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item10 = models.BooleanField(default=True)
    fc1_item10_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item11 = models.BooleanField(default=True)
    fc1_item11_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_item12 = models.BooleanField(default=True)
    fc1_item12_comm = models.CharField(max_length=150, default=' ', blank=True)
    fc1_review = models.CharField(max_length=150, default=' ')
    fc1_review_pdg = models.CharField(max_length=150, default=' ')
