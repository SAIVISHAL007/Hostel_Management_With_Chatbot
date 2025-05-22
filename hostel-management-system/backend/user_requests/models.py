from django.db import models

class Request(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    room_type = models.CharField(max_length=50)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected')
        ],
        default='Pending'
    )
    message = models.TextField(blank=True, null=True)  # Optional message field

    def __str__(self):
        return f"{self.student_name} - {self.room_type} - {self.status}"