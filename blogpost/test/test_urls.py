from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blogpost.views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate

# テスト内容は、「特定のURLでの動作が、そのURLのViewと一致しているか」です。


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class, BlogList)

    def test_detail_url_is_resolved(self):
        url = reverse('detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogDetail)

    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class, BlogCreate)

    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogDelete)

    def test_update_url_is_resolved(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogUpdate)
