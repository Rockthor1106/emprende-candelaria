from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from haztever.business.models import BusinessProfile

class Review(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(verbose_name="Content of the review")
    score = models.PositiveIntegerField(
        help_text="Score should be between 1 and 5",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    username = models.CharField(max_length=100, verbose_name="Review author username")
    email = models.EmailField()
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name='reviews')

class ReviewPhoto(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='review_photos/', blank=True, null=True)