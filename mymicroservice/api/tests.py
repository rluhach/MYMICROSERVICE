# api/tests.py
from django.urls import reverse_lazy
from django.test import TestCase
from .models import Item

class ItemViewTest(TestCase):
    def test_items_listed(self):
        response = self.client.get(reverse_lazy('item-list-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('item-list-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_does_not_use_template(self):
        response = self.client.get(reverse_lazy('item-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response)
