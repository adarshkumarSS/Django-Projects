from django.utils.text import slugify
import uuid

def generate_slug(title:str)->str:
    from vege.models import receipes
    title = slugify(title)

    while(receipes.objects.filter(slug= title).exists()):
        title = f'{slugify(title)} - {str(uuid.uuid4())[:4]}'

    return title
