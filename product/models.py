from django.db import models

# Create your models here.


class ItemType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    file = models.ImageField(upload_to='item_images')
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=[
            ('detail_1', 'Detailed Image 1'),
            ('detail_2', 'Detailed Image 2'),
            ('other', 'Other'),
        ],
    )


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    attributes = models.TextField(blank=True)
    thumbnail = models.ImageField(blank=True)
    images = models.ManyToManyField(Image)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturing_cost = models.DecimalField(max_digits=10, decimal_places=2)


class ItemSizes(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.size} ({self.stock})"


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Description(models.Model):
    text = models.TextField()


class ItemFeature(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)


class Inventory(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sizes = models.ForeignKey(ItemSizes, on_delete=models.CASCADE)


class InventoryLog(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    adjustment = models.IntegerField()
    type = models.CharField(max_length=50)
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Item)
    delivery_provider = models.CharField(max_length=100)
    delivery_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    tracking_id = models.CharField(max_length=100)
    total_product_value = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
