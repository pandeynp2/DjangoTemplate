from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.utils.cache import get_cache_key, learn_cache_key

class CacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Only cache responses to safe HTTP methods (GET, HEAD) and check if response has content attribute
        if request.method in ['GET', 'HEAD'] and hasattr(response, 'content'):
            cache_key = get_cache_key(request, key_prefix='site-cache')
            if not cache_key:
                # We assume response is ready to cache without rendering
                cache_key = learn_cache_key(request, response, key_prefix='site-cache')
                cache.set(cache_key, response.content)

        return response
