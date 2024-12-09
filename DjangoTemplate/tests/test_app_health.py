from django.test import TestCase
from django.urls import reverse


class AppHealthTest(TestCase):
    def test_home_page_status_code(self):
        payload = {}
        response = self.client.post(reverse('app-health'), data=payload)
        self.assertEqual(response.status_code, 200)
