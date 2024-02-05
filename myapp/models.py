from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registry = models.DateField()

    def __str__(self):
        return (f'Username: {self.name}, '
                f'email: {self.email}, '
                f'phone: {self.phone}, '
                f'address: {self.address}, '
                f'date_registry: {self.date_registry}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    how_many = models.IntegerField()
    date_create = models.DateField()
    photo = models.ImageField()

    def __str__(self):
        return (f'name: {self.name}, '
                f'price: {self.price}, '
                f'description: {self.description}, '
                f'how_many: {self.how_many}, '
                f'date_create: {self.date_create}, '
                f'photo: {self.photo}')


class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def get_order_week(self):
        week = self.date_ordered.day
        products = Orders.objects.get(id=self.pk).products.all()
        if 1 <= week <= 7:
            return (f'Заказ от {self.date_ordered}: {", ".join([p.name for p in products])}')
        else:
            return ''

    def get_order_month(self):
        month = self.date_ordered.month
        products = Orders.objects.get(id=self.pk).products.all()
        if month == 1:
            return (f'Заказ от {self.date_ordered}: {", ".join([p.name for p in products])}')
        else:
            return ''

    def get_order_year(self):
        print(self.date_ordered.day)
        year = self.date_ordered.year
        products = Orders.objects.get(id=self.pk).products.all()
        if year == 2008:
            return (f'Заказ от {self.date_ordered}: {", ".join([p.name for p in products])}')
        else:
            return ''

    def get_order_all_time(self):
        products = Orders.objects.get(id=self.pk).products.all()
        return (f'Заказ от {self.date_ordered}: {", ".join([p.name for p in products])}')
