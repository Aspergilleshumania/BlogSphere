from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args, **kwargs):
        
        
        Category.objects.all().delete()
        
        
        categories = ["Sports","Travel","Business","Science"]


        
        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))