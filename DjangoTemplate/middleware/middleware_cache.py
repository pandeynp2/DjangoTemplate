from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.utils.cache import get_cache_key, learn_cache_key

class CacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """Return cached response for safe HTTP methods if available."""
        if request.method in ["GET", "HEAD"]:
            cache_key = get_cache_key(request, key_prefix="site-cache")
            if cache_key:
                cached_response = cache.get(cache_key)
                if cached_response:
                    return cached_response

    def process_response(self, request, response):
        """Cache responses for safe HTTP methods."""
        if request.method in ["GET", "HEAD"] and hasattr(response, "content"):
            cache_key = get_cache_key(request, key_prefix="site-cache")
            if not cache_key:
                cache_key = learn_cache_key(request, response, key_prefix="site-cache")
            cache.set(cache_key, response)

        return response
