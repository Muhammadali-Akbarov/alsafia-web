from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response




class CartAPIView(APIView):
    def post(self, request, *args, **kwargs) -> dict:
        print(request.data)
        print(request.user.id)
        
        return Response(data={'status': 'success'}, status=status.HTTP_200_OK)
