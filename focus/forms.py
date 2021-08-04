from django import forms
from django.contrib.auth.models import User
from focus.models import UserProfileInfo, FocusPlan1, FocusTeach1, FocusEvaluation1, FocusComplex1


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, )

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        help_texts = {
            'username': None,
            'email': None,
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('user_middlename', 'user_level')


class FocusPlan1Form(forms.ModelForm):
    class Meta():
        model = FocusPlan1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'fp1_lessontopic', 'fp1_item1', 'fp1_item2',
            'fp1_item3', 'fp1_item4', 'fp1_item5', 'fp1_item6', 'fp1_item7', 'fp1_review', 'fp1_additional',
            'fp1_review_pdg')


class FocusTeach1Form(forms.ModelForm):
    class Meta():
        model = FocusTeach1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'ft1_lessontopic', 'ft1_item1', 'ft1_item2',
            'ft1_item3', 'ft1_item4', 'ft1_item5', 'ft1_item6', 'ft1_review', 'ft1_additional',
            'ft1_review_pdg')


class FocusEvaluation1Form(forms.ModelForm):
    class Meta():
        model = FocusEvaluation1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'fe1_lessontopic', 'fe1_item1', 'fe1_item2',
            'fe1_item3', 'fe1_item4', 'fe1_item5', 'fe1_review', 'fe1_additional',
            'fe1_review_pdg')


class FocusComplex1Form(forms.ModelForm):
    class Meta():
        model = FocusComplex1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'fc1_lessontopic', 'fc1_item1', 'fc1_item2',
            'fc1_item3', 'fc1_item4', 'fc1_item5', 'fc1_item6', 'fc1_item7', 'fc1_item8', 'fc1_item9', 'fc1_item10',
            'fc1_item11', 'fc1_item12', 'fc1_review',
            'fc1_review_pdg')
