from drf_yasg import openapi

app_health_payload_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['services'],
            properties={
                'services': openapi.Schema(type=openapi.TYPE_OBJECT, description='app services'),
            },
            example={
                "services": ["api"]
            }
)

app_health_response_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'alive': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='app services'),
            },
            example={
                "alive": True
            })
