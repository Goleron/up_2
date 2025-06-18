from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    PICKUP_CHOICES = [
        ('store', 'Самовывоз из магазина'),
        ('courier', 'Курьер'),
        ('post', 'Почта'),
    ]
    pickup_method = models.CharField(
        max_length=20,
        choices=PICKUP_CHOICES,
        default='store'
    )

    def __str__(self):
        return f"Заказ #{self.id} - {self.user.username if self.user else 'Без пользователя'}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        permissions = [
            ("can_view_order", "Can view order"),
            ("can_add_order", "Can add order"),
            ("can_change_order", "Can change order"),
            ("can_delete_order", "Can delete order"),
        ]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
        permissions = [
            ("can_view_orderitem", "Can view order item"),
            ("can_add_orderitem", "Can add order item"),
            ("can_change_orderitem", "Can change order item"),
            ("can_delete_orderitem", "Can delete order item"),
        ]

class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to='images/teams/%Y/%m/%d', blank=True, null=True, verbose_name='Логотип команды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        permissions = [
            ("can_view_team", "Can view team"),
            ("can_add_team", "Can add team"),
            ("can_change_team", "Can change team"),
            ("can_delete_team", "Can delete team"),
        ]

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        permissions = [
            ("can_view_category", "Can view category"),
            ("can_add_category", "Can add category"),
            ("can_change_category", "Can change category"),
            ("can_delete_category", "Can delete category"),
        ]

class Collection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название коллекции')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    year = models.PositiveIntegerField(default=2025, verbose_name='Год коллекции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        permissions = [
            ("can_view_collection", "Can view collection"),
            ("can_add_collection", "Can add collection"),
            ("can_change_collection", "Can change collection"),
            ("can_delete_collection", "Can delete collection"),
        ]

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название производителя')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        permissions = [
            ("can_view_manufacturer", "Can view manufacturer"),
            ("can_add_manufacturer", "Can add manufacturer"),
            ("can_change_manufacturer", "Can change manufacturer"),
            ("can_delete_manufacturer", "Can delete manufacturer"),
        ]

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    photo = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=True, null=True, verbose_name='Фото товара')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='products', verbose_name='Команда')
    collection = models.ManyToManyField(Collection, blank=True, related_name='products', verbose_name='Коллекции')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='products', verbose_name='Производитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = [
            ("can_view_product", "Can view product"),
            ("can_add_product", "Can add product"),
            ("can_change_product", "Can change product"),
            ("can_delete_product", "Can delete product"),
        ]

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'
        permissions = [
            ("can_view_inventory", "Can view inventory"),
            ("can_add_inventory", "Can add inventory"),
            ("can_change_inventory", "Can change inventory"),
            ("can_delete_inventory", "Can delete inventory"),
        ]

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=5)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f"Отзыв на {self.product.name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        permissions = [
            ("can_view_review", "Can view review"),
            ("can_add_review", "Can add review"),
            ("can_change_review", "Can change review"),
            ("can_delete_review", "Can delete review"),
        ]

class Promotion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название акции')
    discount_percent = models.FloatField(verbose_name='Процент скидки')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    products = models.ManyToManyField(Product, blank=True, related_name='promotions', verbose_name='Товары в акции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        permissions = [
            ("can_view_promotion", "Can view promotion"),
            ("can_add_promotion", "Can add promotion"),
            ("can_change_promotion", "Can change promotion"),
            ("can_delete_promotion", "Can delete promotion"),
        ]