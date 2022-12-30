from django import forms

from cabinet_parents.models import Subject, Program, EducationTime, OnlinePlatform, Survey, Region, City, District, \
    TutorRegion, StudentRegion, Test


class SurveyForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        label='Предметы',
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    programs = forms.ModelMultipleChoiceField(
        label='Программа обучения',
        queryset=Program.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    tests = forms.ModelMultipleChoiceField(
        label='Тесты',
        queryset=Test.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    education_time = forms.ModelChoiceField(
        label='Время для занятий',
        queryset=EducationTime.objects.all(),
        initial='New'
    )
    online = forms.ModelMultipleChoiceField(
        label='Онлайн платформы',
        queryset=OnlinePlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Survey
        fields = ('subjects', 'programs', 'tests', 'education_time', 'min_cost', 'max_cost', 'online')

        widgets = {
            'min_cost': forms.NumberInput(attrs={'step': '500'}),
            'max_cost': forms.NumberInput(attrs={'step': '500'}),
        }


class TutorRegionForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        label='Область',
        queryset=Region.objects.all(),
        initial='New'
    )
    city = forms.ModelChoiceField(
        label='Город',
        queryset=City.objects.all(),
        initial='New'
    )
    district = forms.ModelChoiceField(
        label='Район',
        queryset=District.objects.all(),
        initial='New'
    )


    class Meta:
        model = TutorRegion
        fields = ('region', 'city', 'district')


class StudentRegionForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        label='Область',
        queryset=Region.objects.all(),
        initial='New'
    )
    city = forms.ModelChoiceField(
        label='Город',
        queryset=City.objects.all(),
        initial='New'
    )
    district = forms.ModelChoiceField(
        label='Район',
        queryset=District.objects.all(),
        initial='New'
    )


    class Meta:
        model = StudentRegion
        fields = ('region', 'city', 'district')