from django.test import TestCase
from task_manager.models import Task

# Create your tests here.
class URLUnitTestCase(TestCase):
    """
    url template testing
    """

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'task_list.html')

    def test_create_page_template(self):
        response = self.client.get('/create/')
        self.assertTemplateUsed(response, 'task_form.html')
