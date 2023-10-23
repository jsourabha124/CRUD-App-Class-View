from django.test import TestCase
from task_manager.models import Task
from task_manager.forms import TaskForm


# Create your tests here.
class FormDataUnitTestCase(TestCase):

    def test_webpage_title_content(self):
        form = Task(title='test')
        self.assertEqual(form.title, "test")

    def test_webpage_description_content(self):
        form = Task(description='Welcome to test case field')
        form.save()
        self.assertEqual(form.description, "Welcome to test case field")

    def test_webpage_completed_content(self):
        form = Task(completed=True)
        form.save()
        self.assertTrue(form.completed)

    def test_title_max_length(self):
        # Create a Task instance with a title longer than 200 characters
        long_title = "A" * 300
        task = Task()
        task.title = long_title
        # Attempt to save the Task instance
        with self.assertRaises(ValueError):
            task.save()
