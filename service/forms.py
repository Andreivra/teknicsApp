from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select
from service.models import Company


class TaskForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        widgets = {
            'company_name': TextInput(attrs={'placeholder': 'Please enter clients name', 'class': 'form-control'}),
            'contact_name': TextInput(attrs={'placeholder': 'Please enter clients contact person name', 'class': 'form-control'}),
            'agent_name': TextInput(attrs={'placeholder': 'Please enter agent name', 'class': 'form-control'}),
            'phone': NumberInput(attrs={'placeholder': 'Please enter contact phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter clients email',  'class': 'form-control'}),
            'task_name': TextInput(attrs={'placeholder': 'Please enter service problem', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter detailed service problem', 'class': 'form-control',
                                           'rows': 5}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'select_status': Select(attrs={'class': 'form-select'}),
            # 'trainer': Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data['email']
        check_emails = Company.objects.filter(email=get_email)
        if check_emails:
            msg = 'Exista deja'
            self._errors['email'] = self.error_class([msg])

        get_date1 = cleaned_data['start_date']
        get_date2 = cleaned_data['end_date']

        if get_date1 > get_date2:
            msg2 = "Nu se poate ca data de inceput sa fie mai mare ca data de sfarsit"
            self._errors['end_date'] = self.error_class([msg2])

        return cleaned_data


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        widgets = {
            'company_name': TextInput(attrs={'placeholder': 'Please enter clients name', 'class': 'form-control'}),
            'contact_name': TextInput(attrs={'placeholder': 'Please enter clients contact person name', 'class': 'form-control'}),
            'agent_name': TextInput(attrs={'placeholder': 'Please enter agent name', 'class': 'form-control'}),
            'phone': NumberInput(attrs={'placeholder': 'Please enter contact phone number', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter clients email',  'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter service problem', 'class': 'form-control',
                                           'rows': 5}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'select_status': Select(attrs={'class': 'form-select'}),
            # 'trainer': Select(attrs={'class': 'form-select'})
        }
