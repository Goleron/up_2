from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название команды')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to='images/teams/%Y/%m/%d', blank=True, null=True, verbose_name='Логотип команды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название коллекции')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    year = models.PositiveIntegerField(default=2025, verbose_name='Год коллекции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название производителя')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    photo = models.ImageField(upload_to='images/products/%Y/%m/%d', blank=True, null=True, verbose_name='Фото товара')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, verbose_name='Команда')
    collection = models.ManyToManyField(Collection, blank=True, verbose_name='Коллекции')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name='Производитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=5)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f"Отзыв на {self.product.name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Promotion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название акции')
    discount_percent = models.FloatField(verbose_name='Процент скидки')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Товары в акции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'