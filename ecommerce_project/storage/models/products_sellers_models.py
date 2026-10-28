from django.db import models
import django.core.validators

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    tax_gst_id = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField()
    business_type = models.CharField(max_length=50)
    average_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    number_of_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    path = models.TextField()

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    weight = models.IntegerField()
    dimensions = models.TextField()
    avg_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_no_of_reviews = models.IntegerField(default=0)


class ProductCategory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'product'], name='unique_category'),
        ]

class ProductSeller(models.Model):
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku_id = models.CharField(max_length=50)
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['seller', 'product'], name='unique_seller'),
        ]