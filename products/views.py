from .models import Product
from .serializers import product_serializer

from rest_framework import viewsets
from sentence_transformers import SentenceTransformer
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
class ProductSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({"error": "No query provided"}, status=400)
        
        query_embedding = model.encode(query)
        products = Product.objects.all()
        results = []

        for p in products:
            sim = cosine_similarity([query_embedding], [p.embedding])[0][0]
            results.append({"title": p.title, "description": p.description, "price": p.price, "score": float(sim)})

        results = sorted(results, key=lambda x: x["score"], reverse=True)[:20]  # top 20
        return Response(results)



class product_viewset(viewsets.ModelViewSet) :
    serializer_class = product_serializer
    queryset = Product.objects.select_related('seller').all()

    def perform_create(self, serializer):
        instance = serializer.save(seller=self.request.user)
        instance.save()
       