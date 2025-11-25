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

@receiver(pre_save, sender=Product)        
def generate_discription_with_ai(sender, instance, **kwargs):
        if not instance.description:
            response = client.chat.completions.create(
            model="x-ai/grok-4.1-fast:free",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates product descriptions."},
                    {"role": "user", "content": f"Generate a detailed product small attractive description for a product named '{instance.product_name}'."}
                ])
                    
            instance.description = response.choices[0].message.content[:-1]
            print("Description generated and saved.")
        print("Description already exists.") 