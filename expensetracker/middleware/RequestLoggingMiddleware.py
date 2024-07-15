from tracker.models import RequestLogs

class RequestLogging:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        
        RequestLogs.objects.create(
            request_info = vars(request),
            request_method = request.method,
            request_path = request.path
        )

        return self.get_response(request)