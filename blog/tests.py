from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import *

# Create your tests here.
class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user (
            username = 'testuser',
            email = 'test@email.local',
            password = 'secret',
        )

        self.post = Post.objects.create (
            title = 'a goot title',
            body = 'nice body content',
            author = self.user,
        )
        