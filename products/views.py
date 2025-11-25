from .models import Product
from .serializers import product_serializer , product_list_serializer
from .services.products_services import (
    product_detail_service,
    list_products_service,
    create_product_service,
    delete_product_service
)
from rest_framework import viewsets
from sentence_transformers import SentenceTransformer, util
import torch
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.metrics.pairwise import cosine_similarity
from .ai_assistant.call_ai import parse_user_query
from .filters import filter_products

import numpy as np

model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')


class product_services_view(APIView) :
    def post(self, request) :
        return create_product_service(request.data)
    def get(self, request, product_id=None) :
        if product_id :
            return product_detail_service(product_id)
        else :
            return list_products_service()
        
    def delete(self, request, product_id) :
        return delete_product_service(product_id)
    

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

class AIShoppingAssistant(APIView):
    def post(self, request):
        user_text = request.data.get("query")

        if not user_text:
            return Response({"error": "Query is required"}, status=400)

        ai_filters = parse_user_query(user_text)
        print("filters:", ai_filters)
        
        products = filter_products(ai_filters)
        print(products)
        
        serializer = product_list_serializer(products, many=True)
        return Response({
            "filters": ai_filters,
            "results": serializer.data
        })
