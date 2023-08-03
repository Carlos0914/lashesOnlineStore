from django import forms
from app.models import Product


class CreateAppointmentForm(forms.Form):
    products = Product.objects.all()
    appointment_date = forms.DateField(
        widget=forms.TextInput(attrs={'style': 'display: none'}), required=True)
    hour = forms.ChoiceField(choices=(), required=True, widget=forms.Select(
        attrs={'style': 'height: 2rem'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
                                   'style': 'height: 2rem'}), max_length=10, )
    service = forms.ChoiceField(choices=list(
        map(lambda x: [x.id, f"{x.name} - ${x.price}MXN"], products)), required=True, widget=forms.Select(attrs={'style': 'height: 2rem'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3}), required=False)
    image = forms.ImageField(required=False)
