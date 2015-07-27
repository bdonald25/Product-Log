from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=40000)
    serial_number = models.CharField(max_length=40000)
    warranty_info = models.CharField(max_length=40000)
    img = models.ImageField(upload_to='product_photos/', null=True)
    pdf = models.FileField(upload_to='product_pdfs/', null=True)

    def __unicode__(self):
       return self.product_name