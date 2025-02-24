
from django.db import models  
from django.contrib import admin  
from django.utils import timezone  # Provides timezone-aware datetime functions
from datetime import timedelta  # Allows for date and time calculations

# Define your models here

class Icecream(models.Model):
    # Define fields for the Icecream model
    
    flavor = models.CharField(max_length=200)
    
    is_available = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    
    def reorder_day(self):
    # Calculate when to reorder the ice cream
    # It adds 5 weeks to the creation date
        return self.created_at + timedelta(weeks=5)

    def __str__(self):
      
        return self.flavor
    

class IcecreamAdmin(admin.ModelAdmin):
    # This class customizes how the Icecream model appears in the admin interface
    
    # list_display defines which fields are shown in the admin GUI
    list_display = ('flavor', 'is_available', 'reorder_day' )
  

    @admin.display(description="Reorder by")
    def reorder_day(self, obj):
        # Display the reorder day in the admin interface
        # The @admin.display decorator allows customization of how it appears
        return obj.reorder_day()

class Order(models.Model):
    # Define fields for the Order model
    
    # ForeignKey creates a many-to-one relationship with Icecream
    # on_delete=models.CASCADE: if an Icecream is deleted, its orders are also deleted
    # related_name='orders' allows accessing orders from an Icecream instance
    icecream = models.ForeignKey(Icecream, on_delete=models.CASCADE, related_name='orders')
    
    number_of_scoops = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.number_of_scoops} scoop(s) of {self.icecream.flavor}"
    
# Register the Icecream model with the admin site
# This makes it visible and editable in the Django admin interface
admin.site.register(Icecream, IcecreamAdmin)