from django.http import JsonResponse

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        path = request.path
        print(f"Request: {method} {path}")

        if 'HTTP_X_REQUEST_ID' not in request.META:
            return JsonResponse({"error": "Missing X-Request-ID header"}, status=400)

        return self.get_response(request)
