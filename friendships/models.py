from django.db import models

class Friendship(models.Model):
    from_ens = models.CharField(max_length=255)
    to_ens = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Ensure no duplicate friendships
        unique_together = ('from_ens', 'to_ens')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.from_ens} ↔ {self.to_ens}"