from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework. response import Response
from .script import url_to_image, get_dominant_color, get_hex_code

# Create your views here.
class GetColourAPIView(APIView):
    def get(self, request):
        url = request.data["url"]
        img = url_to_image(url)
        colours = get_dominant_color(img)
        dom_code = get_hex_code(colours)

        resp = {
            'logo_border': dom_code,
            'dominant_color': dom_code
        }

        return Response(resp, status = 200)






