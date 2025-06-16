from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from .constants import RATTING_CHOICES

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    category = models.ManyToManyField(Category, related_name= 'books')
    image = models.ImageField(upload_to='books/images/', null=True, blank=True) # to save the uploaded image specifically to the app's inner media directory you need to comment out the MEDIA_ROOT = BASE_DIR / 'media' at settings.py

    def __str__(self):
        return f'{self.id} {self.title}' 
    
    @property
    def is_borrowed(self):
        return self.borrows.filter(return_date__isnull=True).exists()
    
    def is_borrowed_by_current_user(self, user):
        return self.borrows.filter(user= user, return_date__isnull=True).exists()
    

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrows")
    balance_after_borrow = models.DecimalField(max_digits= 12, decimal_places=2)
    balance_after_return = models.DecimalField(null=True, blank=True, default=None, max_digits= 12, decimal_places=2)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.user}"
    
    @property
    def is_returned(self):
        return self.return_date is not None


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name= "reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    ratting = models.CharField(max_length=20, choices= RATTING_CHOICES, default= '1')
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book} - {self.user}"