from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    image = req
    return Response({"message": "Hello, world!"})