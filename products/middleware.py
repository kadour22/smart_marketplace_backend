import time

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        end = time.time()
        duration = (end - start) * 1000 

        print(f"[REQUEST TIME] {request.path} took {duration:.2f} ms")

        return response
