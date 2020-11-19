from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='구매자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    userid = models.CharField(
        max_length=64, verbose_name='구매자아이디', default='None'
    )
    countprice = models.IntegerField(verbose_name='상품가격', default='0')
    price = models.IntegerField(verbose_name='총가격', default='0')
    quantity = models.IntegerField(verbose_name='수량')
    address = models.CharField(
        max_length=128, verbose_name='구매자주소', default="None", null=False)
    productimg = models.CharField(
        max_length=64, verbose_name='상품이미지', default='None')
    orderdate = models.DateTimeField(auto_now_add=True, verbose_name='구매일')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'practice_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
