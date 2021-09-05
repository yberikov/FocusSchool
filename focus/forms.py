from django import forms
from django.contrib.auth.models import User
from focus.models import UserProfileInfo, FocusPlan1, FocusTeach1, FocusEvaluation1, FocusComplex1, Pdg


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
            'fp1_item2_comm', 'fp1_item3', 'fp1_item3_comm', 'fp1_item4', 'fp1_item5', 'fp1_item5_comm', 'fp1_item6',
            'fp1_item6_comm', 'fp1_item7', 'fp1_item7_comm', 'fp1_review', 'fp1_additional',
            'fp1_review_pdg')
        widgets = {
            'subject': forms.Select(attrs={'class': 'js-select2'}),
            'schoolyear': forms.Select(attrs={'class': 'js-select2'}),
            'pdg': forms.Select(attrs={'class': 'js-select2'}),
            'classes': forms.Select(attrs={'class': 'js-select2'}),
            'fp1_lessontopic': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fp1_item1': forms.Select(attrs={'class': 'js-select2'}),
            'fp1_item2': forms.CheckboxInput(attrs={'class': 'check'}),
            'fp1_item3': forms.CheckboxInput(attrs={'class': 'check'}),
            'fp1_item4': forms.Select(attrs={'class': 'js-select2'}),
            'fp1_item5': forms.CheckboxInput(attrs={'class': 'check'}),
            'fp1_item6': forms.CheckboxInput(attrs={'class': 'check'}),
            'fp1_item7': forms.CheckboxInput(attrs={'class': 'check'}),
            'fp1_review': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fp1_additional': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fp1_review_pdg': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

        }


class FocusTeach1Form(forms.ModelForm):
    class Meta():
        model = FocusTeach1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'ft1_lessontopic', 'ft1_item1', 'ft1_item2',
            'ft1_item2_comm', 'ft1_item3', 'ft1_item3_comm', 'ft1_item4', 'ft1_item5', 'ft1_item5_comm', 'ft1_item6',
            'ft1_review', 'ft1_additional',
            'ft1_review_pdg')
        widgets = {
            'subject': forms.Select(attrs={'class': 'js-select2'}),
            'schoolyear': forms.Select(attrs={'class': 'js-select2'}),
            'pdg': forms.Select(attrs={'class': 'js-select2'}),
            'classes': forms.Select(attrs={'class': 'js-select2'}),
            'ft1_lessontopic': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ft1_item1': forms.Select(attrs={'class': 'js-select2'}),
            'ft1_item2': forms.CheckboxInput(attrs={'class': 'check'}),
            'ft1_item3': forms.CheckboxInput(attrs={'class': 'check'}),
            'ft1_item4': forms.Select(attrs={'class': 'js-select2'}),
            'ft1_item5': forms.CheckboxInput(attrs={'class': 'check'}),
            'ft1_item6': forms.Select(attrs={'class': 'js-select2'}),
            'ft1_review': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ft1_additional': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ft1_review_pdg': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

        }


class FocusEvaluation1Form(forms.ModelForm):
    class Meta():
        model = FocusEvaluation1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'fe1_lessontopic', 'fe1_item1', 'fe1_item1_comm',
            'fe1_item2',
            'fe1_item2_comm', 'fe1_item3', 'fe1_item3_comm', 'fe1_item4', 'fe1_item4_comm', 'fe1_item5',
            'fe1_item5_comm', 'fe1_review', 'fe1_additional',
            'fe1_review_pdg')
        widgets = {
            'subject': forms.Select(attrs={'class': 'js-select2'}),
            'schoolyear': forms.Select(attrs={'class': 'js-select2'}),
            'pdg': forms.Select(attrs={'class': 'js-select2'}),
            'classes': forms.Select(attrs={'class': 'js-select2'}),
            'fe1_lessontopic': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fe1_item1': forms.CheckboxInput(attrs={'class': 'check'}),
            'fe1_item2': forms.CheckboxInput(attrs={'class': 'check'}),
            'fe1_item3': forms.CheckboxInput(attrs={'class': 'check'}),
            'fe1_item4': forms.CheckboxInput(attrs={'class': 'check'}),
            'fe1_item5': forms.CheckboxInput(attrs={'class': 'check'}),
            'fe1_review': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fe1_additional': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fe1_review_pdg': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

        }


class FocusComplex1Form(forms.ModelForm):
    class Meta():
        model = FocusComplex1
        fields = (
            'user_teacher', 'subject', 'schoolyear', 'pdg', 'classes', 'fc1_lessontopic', 'fc1_item1', 'fc1_item2',
            'fc1_item3', 'fc1_item4', 'fc1_item5', 'fc1_item6', 'fc1_item7', 'fc1_item8', 'fc1_item9', 'fc1_item10',
            'fc1_item11', 'fc1_item12', 'fc1_review',
            'fc1_review_pdg', 'fc1_item2_comm', 'fc1_item3_comm', 'fc1_item4_comm', 'fc1_item6_comm',
            'fc1_item8_comm', 'fc1_item9_comm', 'fc1_item10_comm', 'fc1_item11_comm', 'fc1_item12_comm',)
        widgets = {
            'subject': forms.Select(attrs={'class': 'js-select2'}),
            'schoolyear': forms.Select(attrs={'class': 'js-select2'}),
            'pdg': forms.Select(attrs={'class': 'js-select2'}),
            'classes': forms.Select(attrs={'class': 'js-select2'}),
            'fc1_lessontopic': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fc1_item1': forms.Select(attrs={'class': 'js-select2'}),
            'fc1_item2': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item3': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item4': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item5': forms.Select(attrs={'class': 'js-select2'}),
            'fc1_item6': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item7': forms.Select(attrs={'class': 'js-select2'}),
            'fc1_item8': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item9': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item10': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item11': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_item12': forms.CheckboxInput(attrs={'class': 'check'}),
            'fc1_review': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'fc1_review_pdg': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

        }
class PdgForm(forms.ModelForm):
    class Meta():
        model = Pdg
        fields = (
            'pdg_goal', 'schoolyear', 'halfyear')
        widgets = {
            'pdg_goal': forms.TextInput(attrs={'class': 'form-control'}),
            'schoolyear': forms.Select(attrs={'class': 'form-control'}),
            'halfyear': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '2'})
        }
