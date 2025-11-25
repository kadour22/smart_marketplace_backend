from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from sentence_transformers import SentenceTransformer
from .ai_assistant.AiInstnace import client
model = SentenceTransformer('all-MiniLM-L6-v2')

@receiver(pre_save , sender=Product)
def embedding_product_field(sender , instance , **kwargs) :
    text = f"{instance.product_name} {instance.description}"
    instance.embedding = model.encode(text).tolist()
    print(f'{instance.embedding[:5]}')

