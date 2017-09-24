from Qbank.models import *
from django import forms


class QuestionBankForm(forms.ModelForm):
    CourseTitle = forms.CharField(widget=forms.Select())
    CourseCode = forms.CharField(widget=forms.Select())

    class Meta:
        model = QuestionBank
        fields = ['level','CourseTitle', 'CourseCode', 'CourseUnit', 'Semester', 'Date', 'question_papers' ]
        

    
    def __init__(self, *args, **kwargs):#Sort interests alphabetically
        super(QuestionBankForm, self).__init__(*args, **kwargs)
        self.fields['CourseTitle'].queryset = CourseRecord.objects.all()
        self.fields['CourseCode'].queryset = CourseRecord.objects.all()
        