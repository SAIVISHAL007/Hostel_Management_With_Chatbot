from django.db import models

class Complaint(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    complaint_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Complaint by {self.student_name} - Status: {self.status}"