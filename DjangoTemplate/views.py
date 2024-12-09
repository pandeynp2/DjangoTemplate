from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import app_health_payload_schema, app_health_response_schema

class AppHealth(APIView):
    @swagger_auto_schema(operation_description="application health",
                         operation_summary="application status",
                         request_body=app_health_payload_schema,
                         tags=['core'],
                         responses={200: app_health_response_schema},)
    def post(self, request, *args, **kwargs):
        return Response({"alive": True}, status=200)

    def get(self, request, *args, **kwargs):
        return Response({"alive": True}, status=200)

