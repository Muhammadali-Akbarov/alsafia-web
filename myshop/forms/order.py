from dataclasses import fields
from django.forms import ModelForm

from myshop.models.customer import CustomerModel


class CustomerModelForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = ('name', 'phone',)

    def __init__(self, *args, **kwargs):
        super(CustomerModelForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'comment-input-box'})
            if name=="phone":
                field.widget.attrs.update({'value': '+998'})