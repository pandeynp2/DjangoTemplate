from django.test import TestCase
from django.urls import reverse
from django.core.cache import cache


class CacheMiddlewareTest(TestCase):
    def setUp(self):
        cache.clear()

    def test_get_response_cached(self):
        url = reverse('app-health')

        # First request stores response in cache
        response1 = self.client.get(url)
        self.assertEqual(response1.status_code, 200)

        # Second request should hit cache and return same content
        response2 = self.client.get(url)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response1.content, response2.content)
