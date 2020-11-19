from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    productimg = models.ImageField(
        blank=True,  upload_to="images", verbose_name='상품이미지', default="None")
    reguser = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='등록자')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pactice_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
