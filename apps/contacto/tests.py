from django.test import TestCase

# Create your tests here.


class ContactoTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('contacto')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
