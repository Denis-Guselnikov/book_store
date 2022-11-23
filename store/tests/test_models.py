from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Проверка атрибутов полей Модели Category
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        Проверка name в Category
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                             slug='django-beginners', price='20.00', image='gjango')

    def test_product_model_entry(self):
        """
        Проверка атрибутов полей Модели Product
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')