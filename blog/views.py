from django.views.generic import ListView
from .models import *

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
