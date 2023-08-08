from django import forms
from app.models import Product


class CreateAppointmentForm(forms.Form):
    products = Product.objects.all()
    appointment_date = forms.DateField(
        widget=forms.TextInput(attrs={'style': 'display: none'}), required=True)
    hour = forms.ChoiceField(choices=(), required=True, widget=forms.Select(
        attrs={'class': 'form-select'}
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=60)
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=10)
    service = forms.ChoiceField(choices=list(
        map(lambda x: [x.id, f"{x.name} - ${x.price}MXN"], products)), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}), required=True)
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control'}))
