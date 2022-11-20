from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    email = models.CharField(max_length=40, null=False)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_pic(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/media/profile_pic/CustomerProfilePic/mouse.jpg"

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


    @staticmethod
    def getAllCategory():
        return Category.objects.all()


class Product(models.Model):
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.id, ])

    # All Product get
    @staticmethod
    def getAllProduct(self):
        return Product.objects.all()

    # Filter Product By Category
    @staticmethod
    def getProductByFilter(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.getAllProduct()

    @staticmethod
    def getProductById(productList):
        return Product.objects.filter(id__in=productList)


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)


class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
