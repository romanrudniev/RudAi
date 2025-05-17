from django.db import models
from django.contrib.auth.models import User

class QueryHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="query_histories"),
    query = models.TextField(),
    response_text = models.TextField(),
    response_image = models.ImageField(upload_to='img/query_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __self__(self):
        return f"Запит від {self.user.username} - {self.created_at.strftime('%d.%m.%Y %H: %M:')}"