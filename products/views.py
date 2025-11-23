from .models import Product
from .serializers import product_serializer

from rest_framework import viewsets
from sentence_transformers import SentenceTransformer, util
import torch
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

class semantic_search(APIView) :
    def get(self, request):
        query = request.query_params.get("q")
        if not query:
            return Response({"error": "Missing query parameter ?q="}, status=400)
        
        query_embedding = model.encode([query])
        
        products = Product.objects.all()
        embedding = [p.embedding for p in products]
        similarities = cosine_similarity(query_embedding , embedding)[0]
        threshold = 0.30

        results = []
        for product, score in zip(products, similarities):
            print(f"Product: {product.product_name}, Score: {score}")
            if score >= threshold:
                results.append({
                    "id": product.id,
                    "name": product.product_name,
                    "similarity": float(score),
                })
      
        results = sorted(results, key=lambda x: x["similarity"], reverse=True)
        results = results[:10] 
        return Response({"results": results})