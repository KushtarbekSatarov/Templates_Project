from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

class Goods(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='goods_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()

    def str(self):
        return self.title

class Feedback(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def str(self):
        return f'{self.author} - {self.goods.title}'