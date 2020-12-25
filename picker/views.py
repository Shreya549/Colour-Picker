from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework. response import Response
from .script import url_to_image, get_dominant_color, get_hex_code

# Create your views here.
class GetColourAPIView(APIView):
    def get(self, request):
        url = request.query_params.get('url', None)
        url = url.replace(' ', '%20')
        img = url_to_image(url)

        x,y,a,b = 0,0,1000,50
        crop_img = img[y:y+b, x:x+a]

        colours = get_dominant_color(img)
        dom_code = get_hex_code(colours)

        colours = get_dominant_color(crop_img)
        border_code = get_hex_code(colours)

        resp = {
            'logo_border': border_code,
            'dominant_color': dom_code
        }

        return Response(resp, status = 200)






