from django import forms



from .models import TodoItem1
"""from .models import MyEmp

class employee_form (forms.Form) :
    empname = forms.CharField(max_length=20)
    empage = forms.IntegerField()
    empaddress = forms.CharField()
    empphno = forms.IntegerField()

class employee_form(forms.ModelForm):
    class meta:
        model = MyEmp
        fields = "__all__"""""


class DateInput(forms.DateInput):
    inputtype='Date'


class data_form(forms.ModelForm):
    class Meta:
        model=TodoItem1
        fields="__all__"
        widgets={
        'Date_And_Time':DateInput(),
        'CreatedModified_at':DateInput()
        }
