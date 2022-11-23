from unittest import skip  # Даёт возможность пропускать тесты

from django.http import HttpRequest
from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass

class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                             slug='django-beginners', price='20.00', image='gjango')

    
    def test_url_allowed_host(self):
        """
        Тест разрешенного хоста
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Тестирование URL модели Product
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Тестирование URL модели Category
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Тестирования шаблона home
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_function(self):
        """
        Пример: Использование RequestFactory
        """
        request = self.factory.get('/item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
