from uuid import uuid4

def generate_name_image(sender, instance, **kwargs):
    if hasattr(instance, 'image') and instance.image:
        filname = instance.image.name
        composition = filname.split('.')
        instance.image.name = f'{composition[0]}-{uuid4()}.{composition[1]}'
