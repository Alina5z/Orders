from django.db import models


class Orders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['created']
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Products(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductsInOrders(models.Model):
    owner = models.ForeignKey('auth.User', related_name='productsinorders', on_delete=models.CASCADE)
    order = models.ForeignKey('Orders', related_name='productsinorders', on_delete=models.CASCADE)
    prod = models.ForeignKey('Products', related_name='productsinorders', on_delete=models.CASCADE)
    quantite = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.owner} {self.prod} {self.quantite} {self.price}'

    class Meta:
        ordering = ['owner']
        verbose_name = "ProductsInOrders"
        verbose_name_plural = "ProductsInOrders"
