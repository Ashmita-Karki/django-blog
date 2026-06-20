from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if os.path.exists("blog_data.json"):
            call_command("loaddata", "blog_data.json")
            self.stdout.write("Data loaded successfully")
        else:
            self.stdout.write("No data file found")