from django.test import TestCase
from .models import Task
from django.urls import reverse

# Create your tests here.
class TaskViewTests(TestCase):
    def setUp(self):
        # Create a task object to be used in tests
        self.task = Task.objects.create(
            title='Test Task',
            due_date='2024-09-30',
            status='pending',
            priority='medium'
        )
    
    def test_create_task(self):
        data = {
            'title': 'New Task',
            'due_date': '2024-09-29',
            'status': 'pending',
            'priority': 'medium'
        }
        response = self.client.post(reverse('task-create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())
    

    def test_update_task(self):
        data = {
            'title': 'Updated Task',
            'due_date': '2024-09-30',
            'status': 'completed',
            'priority': 'high'
        }
        response = self.client.post(reverse('task-update', args=[self.task.id]), data)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.status, 'completed')

    def test_view_task(self):
        response = self.client.get(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.title)
    
    def test_delete_task(self):
        response = self.client.post(reverse('task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

        
        