from django.db import models

# Create your models here.


BOOK_CATEGORY = (
    ("Health", "Health"),
    ("Games", "Games"),
    ("Meetups", "Meetups"),
    ("Music", "Music"),
    ("Art", "Art"),
    ("Food", "Food"),
    ("Business", "Business"),
    ("Sports", "Sports"),
)


class Book(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	name = models.CharField(max_length=80)
	author = models.CharField(max_length=80)
	price = models.CharField(max_length=12)
	category = models.CharField(max_length=20, choices=BOOK_CATEGORY)
	date = models.DateField(auto_now_add=True)
	is_available = models.BooleanField()
	#image = models.ImageField()


	def __str__(self):
		return str(self.name)


class Order(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	book = models.ForeignKey(Book, on_delete=models.PROTECT)
	book_user = models.IntegerField()
	order_date = models.DateField(auto_now_add=True)
	deliver = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user)


