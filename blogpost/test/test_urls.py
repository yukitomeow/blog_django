from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blogpost.views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate


class TestUrls(SimpleTestCase):
    def test_list_uri_is_resolved(self):
        url = reverse('list')
        # I dont understnd what .func.vew_class is
        self.assertEquals(resolve(url).func.view_class, BlogList)
