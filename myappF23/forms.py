from django import forms
from django.forms import ModelForm, SelectDateWidget
from myappF23.models import Order

class InterestForm(forms.Form):
    INTEREST_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )

    interested = forms.ChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.RadioSelect
    )

    levels = forms.IntegerField(
        min_value=1,
        initial=1  # Correct the typo here
    )

    comments = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='Additional Comments'
    )
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['student', 'course', 'levels', 'order_date']
        widgets = {
            'student': forms.RadioSelect,
            'order_date': SelectDateWidget(),
        }