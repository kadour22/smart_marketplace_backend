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

class ProductSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get("q")
        if not query:
            return Response({"error": "Missing query parameter ?q="}, status=400)
        
        # Determine device
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        
        # Encode query and keep on device
        query_embedding = model.encode(query, convert_to_tensor=True, device=device)
        print(query_embedding)
        
        products = Product.objects.all()
        results = []
        
        for p in products:
            try:
                # Move product embedding to the same device as query_embedding
                product_embedding = torch.tensor(p.embedding, device=device)
                
                similarity = util.cos_sim(query_embedding, product_embedding).item()
                print(f"{p.product_name}: {similarity:.3f}")
                
                # Only keep high similarity results
                if similarity >= 0.6:
                    results.append({
                        "id": p.id,
                        "product_name": p.product_name,
                        "description": p.description,
                        "price": p.price,
                        "similarity": round(similarity, 3),
                    })
            except Exception as e:
                print(f"Error with {p.product_name}: {e}")
        
        results = sorted(results, key=lambda x: x["similarity"], reverse=True)
        
        if not results:
            return Response({"message": "No similar products found"}, status=404)
        
        return Response(results)

class product_viewset(viewsets.ModelViewSet) :
    serializer_class = product_serializer
    queryset = Product.objects.select_related('seller').all()

    def perform_create(self, serializer):
        instance = serializer.save(seller=self.request.user)
        instance.save()
       