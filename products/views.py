# rest_framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# local imports
from .models import Product
from .serializers import product_serializer , product_list_serializer

from .services.products_services import (
    product_detail_service,
    list_products_service,
    create_product_service,
    delete_product_service,
    add_to_wishlist_service,
    my_wishlist_service,
    remove_from_wishlist_service,
)
# AI and search imports
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .ai_assistant.call_ai import parse_user_query
from .filters import filter_products

model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

class product_services_view(APIView) :
    
    def post(self, request) :
        return create_product_service(request.data)
    def get(self, request) :
        return list_products_service()
    def delete(self, request, product_id) :
        return delete_product_service(product_id)
    
class product_detail_view(APIView) :
    def get(self, request, product_id) :
        product = Product.objects.get(id=product_id)
        if not product :
            return Response(
                {"error" : "product not found"} , status=404
            )
        serializer = product_serializer(product)    
        return Response(serializer.data)

class semantic_search(APIView) :
    permission_classes = [IsAuthenticated]
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
                    "image":product.image,
                    "similarity": float(score),
                })
      
        results = sorted(results, key=lambda x: x["similarity"], reverse=True)
        results = results[:10] 
        return Response({"results": results})

class AIShoppingAssistant(APIView):
    permission_classes = [IsAuthenticated]
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

class WishlistServiceView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, product_id):
        user = request.user
        return add_to_wishlist_service(user, product_id)
    def get(self, request):
        user = request.user
        return my_wishlist_service(user)

class DeleteProductFromWishlistView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, product_id):
        user = request.user
        return remove_from_wishlist_service(user, product_id)