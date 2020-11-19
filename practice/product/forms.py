from django import forms
from .models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요'
        }, max_length=63, label='상품명'
    )
    price = forms.IntegerField(
        error_messages={
            'required': '가격을 입력해주세요.'
        }, label='상품가격'
    )
    description = forms.CharField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        }, label='상품설명'
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     price = cleaned_data.get('price')
    #     description = cleaned_data.get('description')

    #     if name and price and description:
    #         product = Product(
    #             name=name,
    #             price=price,
    #             description=description
    #         )

    #         product.save()
