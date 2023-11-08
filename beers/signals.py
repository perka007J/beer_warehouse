from django.db.models.signals import pre_save
from utils.images import generate_name_image
from .models import Beer

pre_save.connect(generate_name_image, Beer)
